import sys
sys.path.append('/Users/annaxu/Desktop')

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from yims_backend.database.base import Base
from yims_backend.database.session import session
from yims_backend.tables.MatchDB import MatchDB
from yims_backend.tables.UserDB import UserDB

class PlayerDB(Base):
    __tablename__ = 'players'
    match_id = Column(Integer, ForeignKey('matches.id'), primary_key=True)
    netid = Column(String(10), ForeignKey('users.netid'), primary_key=True)
    match = relationship("MatchDB", backref="players")
    user = relationship("UserDB", backref="players")

    def save(self):
        session.add(self)
        session.commit()