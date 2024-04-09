import sys
sys.path.append('/Users/annaxu/Desktop')

from yims_backend.database.session import session
from yims_backend.models.CollegeDB import CollegeDB
from yims_backend.business.College import College
from yims_backend.business.Match import Match

class CollegeDAO:
    @classmethod
    def get_all_colleges_alphabetical(cls):
        colleges = session.query(CollegeDB).order_by(CollegeDB.name).all()
        return [College(college.name, college.abbreviation, college.points) for college in colleges]

    @classmethod
    def get_leaderboard(cls):
        colleges = session.query(CollegeDB).order_by(CollegeDB.points.desc()).all()
        return [College(college.name, college.abbreviation, college.points) for college in colleges]
    
    @classmethod
    def get_college_id(cls, college_name):
        college = session.query(CollegeDB).filter_by(name=college_name).first()
        if college:
            return college.id
        return None
    
    @classmethod
    def get_college_by_id(cls, college_id):
        college = session.query(CollegeDB).filter_by(id=college_id).first()
        if college:
            return College(college.name, college.abbreviation, college.points)
        return None

    @classmethod
    def get_college_by_name(cls, college_name):
        college = session.query(CollegeDB).filter_by(name=college_name).first()
        if college:
            return College(college.name, college.abbreviation, college.points)
        return None

    @classmethod
    def add_points_to_college(cls, college_name, additional_points):
        college = session.query(CollegeDB).filter_by(name=college_name).first()
        if college:
            college.points += additional_points
            session.commit()

    @classmethod
    def get_matches_by_college(cls, college_name):
        college = session.query(CollegeDB).filter_by(name=college_name).first()
        if college:
            matches = college.matches.all()  # Assuming you have a relationship defined in CollegeDB
            return [Match(match.college1.name, match.college2.name, match.sport.name, match.location, match.date, match.start_time, match.college_pts1, match.college_pts2, match.ref) for match in matches]
        return []
