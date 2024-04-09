import sys
sys.path.append('/Users/annaxu/Desktop')

from datetime import datetime, timedelta
from sqlalchemy import and_, or_, func
from yims_backend.database.session import session
from yims_backend.models.MatchDB import MatchDB
from yims_backend.business.Match import Match
from yims_backend.data_access.CollegeDataAccess import CollegeDAO
from yims_backend.data_access.SportsDataAccess import SportsDAO
from yims_backend.data_access.UsersDataAccess import UsersDAO
from yims_backend.consts import colleges_ids
from yims_backend.consts import sports_ids

class MatchDAO:
    
    @classmethod
    def is_college_available(cls, college_id, date, start_time, location=None):
        # Convert start_time to a datetime object for easier manipulation
        start_time_obj = datetime.strptime(start_time, '%H:%M')
        # Calculate the end time based on the duration (in hours)
        end_time_obj = start_time_obj + timedelta(hours=1)

        # Query for matches involving the college on the given date and time range
        existing_match = session.query(MatchDB).filter(
            and_(
                # Check if the college is either college_id1 or college_id2 in the match
                or_(MatchDB.college_id1 == college_id, MatchDB.college_id2 == college_id),
                # Check if the match is on the same date
                MatchDB.date == date,
                # Check if the match time overlaps with the requested time range
                MatchDB.start_time < end_time_obj.strftime('%H:%M'),
                # Match should start before the end time of the requested time range
                MatchDB.start_time >= start_time,
                # Check if the location is the same (if a location is provided)
                MatchDB.location == location if location else True
            )
        ).first()
        if existing_match:
            if existing_match.college_id1 == college_id or existing_match.college_id2 == college_id:
                return False, "College is already scheduled for a match at this time."
            if location and existing_match.location == location:
                return False, "Location is already in use at this time."
        return True, "College and location are available."

    @classmethod
    def get_filtered_matches(cls, college=None, sport=None):
        query = session.query(MatchDB)

        if college:
            query = query.filter(or_(MatchDB.college_id1 == college.id, MatchDB.college_id2 == college.id))

        if sport:
            query = query.filter(MatchDB.sport_id == sport.id)

        matches = query.all()
        return [Match(college1=CollegeDAO.get_college_by_id(match.college_id1),
                      college2=CollegeDAO.get_college_by_id(match.college_id2),
                      sport=SportsDAO.get_sport_by_id(match.sport_id),
                      location=match.location,
                      date=match.date,
                      start_time=match.start_time,
                      college1_pts=match.college_pts1,
                      college2_pts=match.college_pts2,
                      ref=UsersDAO.get_user_by_netid(match.ref_id)) for match in matches]

    @classmethod
    def add_match(cls, college_name_1, college_name_2, sport, location, date, start_time):
        college_id1 = CollegeDAO.get_college_id(college_name_1)
        college_id2 = CollegeDAO.get_college_id(college_name_2)
        sport_id = SportsDAO.get_sport_id(sport)
        if cls.is_college_available(college_id1, date, start_time) and cls.is_college_available(college_id2, date, start_time):
            match = MatchDB(college_id1=college_id1, college_id2=college_id2, sport_id=sport_id, location=location, date=date, start_time=start_time)
            session.add(match)
            session.commit()
            return True
        else:
            return False

    @classmethod
    def delete_match(cls, match_id):
        match = session.query(MatchDB).filter_by(id=match_id).first()
        if match:
            session.delete(match)
            session.commit()

    @classmethod
    def get_past_unscored_matches(cls):
        current_date = datetime.now().strftime