import sys
sys.path.append('/Users/annaxu/Desktop')

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from yims_backend.database.base import Base
from yims_backend.database.session import session

class PlayerDB(Base):
    __tablename__ = 'players'
    match_id = Column(Integer, ForeignKey('matches.id'), primary_key=True)
    netid = Column(String(10), ForeignKey('users.netid'), primary_key=True)
    user = relationship("UserDB", back_populates="player_entries")
    match = relationship("MatchDB", back_populates="players")

    def save(self):
        session.add(self)
        session.commit()