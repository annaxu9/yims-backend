import sys
sys.path.append('/Users/annaxu/Desktop')

from yims_backend.database.session import session
from yims_backend.tables.UserDB import UserDB
from yims_backend.models.User import User

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
    def add_user(self, user):
        userdb = UserDB(netid=user.netid, firstname=user.firstname, lastname=user.lastname, college=user.college, role=user.role, points=user.points)
        session.add(userdb)
        session.commit()

    def get_user(self, netid):
        user = session.query(UserDB).filter(UserDB.netid == netid).first()
        if user:
            return User(user.netid, user.firstname, user.lastname, get_college_name(user.college_id), user.role).to_dict()