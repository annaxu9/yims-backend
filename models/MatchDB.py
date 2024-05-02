import sys
sys.path.append('/Users/annaxu/Desktop')

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from yims_backend.database.base import Base
from yims_backend.database.session import session
from yims_backend.models.PlayerDB import PlayerDB
from yims_backend.models.CollegeDB import CollegeDB
from yims_backend.models.SportDB import SportDB
from yims_backend.models.UserDB import UserDB

class MatchDB(Base):
    __tablename__ = 'matches'
    id = Column(Integer, primary_key=True, autoincrement=True)
    college_id1 = Column(Integer, ForeignKey('colleges.id'))
    college_id2 = Column(Integer, ForeignKey('colleges.id'))
    college_pts1 = Column(Integer, default=-1)
    college_pts2 = Column(Integer, default=-1)
    sport_id = Column(Integer, ForeignKey('sports.id'))
    location = Column(String(20))
    date = Column(String(10))
    start_time = Column(String(10))
    # match_code = Column(Integer(10))
    ref_id = Column(String(10), ForeignKey('users.netid'))

    # Use string references for relationships to avoid circular imports
    sport = relationship("SportDB", backref="matches")
    college1 = relationship("CollegeDB", foreign_keys=[college_id1])
    college2 = relationship("CollegeDB", foreign_keys=[college_id2])
    ref = relationship("UserDB", foreign_keys=[ref_id])
    players = relationship("PlayerDB", back_populates="match")
    
    def save(self):
        session.add(self)
        session.commit()
