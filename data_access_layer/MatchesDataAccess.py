import sys
sys.path.append('/Users/annaxu/Desktop')

from yims_backend.database.session import session
from yims_backend.tables.MatchDB import MatchDB
from yims_backend.models.Match import Match
from yims_backend.data_access_layer.CollegeDataAccess import CollegeDAO
from yims_backend.consts import colleges_ids
from yims_backend.consts import sports_ids

class MatchDAO:
    def get_all_matches(self):
        matches = session.query(MatchDB).all().order_by(MatchDB.date)
        return [Match(match.team1, match.team2, match.team1_score, match.team2_score, match.date) for match in matches]
    def add_match(self, college_name_1, college_name_2, sport, location, date, start_time):
        college1 = colleges_ids[college_name_1]
        college2 = colleges_ids[college_name_2]
        sportid = sports_ids[sport]
        match = MatchDB(college_id1=college1, college_id2=college2, sport_id=sportid, location=location, date=date, start_time=start_time)
        session.add(match)
        session.commit()
    def update_match(self, match_id, team1, team2, team1_score, team2_score, date):
        match = session.query(MatchDB).filter_by(id=match_id).first()
        if match:
            match.team1 = team1
            match.team2 = team2
            match.team1_score = team1_score
            match.team2_score = team2_score
            match.date = date
            session.commit()
    def delete_match(self, match_id):
        match = session.query(MatchDB).filter_by(id=match_id).first()
        if match:
            session.delete(match)
            session.commit()