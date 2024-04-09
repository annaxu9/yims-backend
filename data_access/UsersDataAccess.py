import sys
sys.path.append('/Users/annaxu/Desktop')

from yims_backend.database.session import session
from yims_backend.models.UserDB import UserDB
from yims_backend.business.User import User
from yims_backend.business.Match import Match

colleges = {
    "Benjamin Franklin" : 'BF', 
    "Berkeley": 'BK', 
    "Branford": 'BR',
    "Davenport": 'DC',
    "Ezra Stiles": 'ES',
    "Grace Hopper": 'GH',
    "Jonathan Edwards": 'JE',
    "Morse": 'MC',
    "Pauli Murray": "MY",
    "Pierson": 'PC',
    "Saybrook": 'SY',
    "Silliman": 'SM',
    "Timothy Dwight": 'TD',
    "Trumbull": 'TC'
}

def get_college_id(college_name):
    return list(colleges).index(college_name) + 1

def get_college_name(college_id):
    return list(colleges)[college_id - 1]

class UsersDAO:
    @classmethod
    def add_user(cls, user):
        userdb = UserDB(netid=user.netid, firstname=user.firstname, lastname=user.lastname, college_id=get_college_id(user.college), role=user.role, points=user.points)
        session.add(userdb)
        session.commit()

    @classmethod
    def get_user_by_netid(cls, netid):
        user = session.query(UserDB).filter_by(netid=netid).first()
        if user:
            return User(user.netid, user.firstname, user.lastname, get_college_name(user.college_id), user.role, points=user.points)
        return None

    @classmethod
    def get_user(cls, netid):
        user = session.query(UserDB).filter(UserDB.netid == netid).first()
        if user:
            return User(user.netid, user.firstname, user.lastname, get_college_name(user.college_id), user.role, points=user.points)
        return None

    @classmethod
    def get_matches_by_user(self, netid):
        user = session.query(UserDB).filter(UserDB.netid == netid).first()
        if user:
            matches = [player_entry.match for player_entry in user.player_entries]
            return matches
        return []

