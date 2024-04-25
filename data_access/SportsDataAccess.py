import sys
sys.path.append('/Users/annaxu/Desktop')

from yims_backend.database.session import session
from yims_backend.models.SportDB import SportDB
from yims_backend.business.Sport import Sport
from yims_backend.business.Match import Match


class SportsDAO:
    @classmethod
    def get_all_sports(cls):
        sports = session.query(SportDB).all()
        return [Sport(sport.id, sport.name, sport.points_for_win, sport.season, sport.icon) for sport in sports]

    @classmethod
    def get_matches_by_sport(cls, sport_name):
        sport = session.query(SportDB).filter_by(name=sport_name).first()
        if sport:
            matches = sport.matches.all()  # Assuming you have a relationship defined in SportDB
            # Assuming you have a Match class that can create match instances from MatchDB objects
            return [Match.from_db(match_db) for match_db in matches]
        return []
    
    @classmethod
    def get_sport_id(cls, sport_name):
        sport = session.query(SportDB).filter_by(name=sport_name).first()
        if sport:
            return sport.id
        return None
    
    @classmethod
    def get_sport_by_id(cls, sport_id):
        return session.query(SportDB).filter_by(id=sport_id).first()
    
    @classmethod
    def get_sport_by_name(cls, sport_name):
        return session.query(SportDB).filter_by(name=sport_name).first()
