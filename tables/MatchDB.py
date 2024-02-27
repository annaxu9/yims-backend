import sys
sys.path.append('/Users/annaxu/Desktop')

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from yims_backend.database.base import Base
from yims_backend.database.session import session
from yims_backend.tables.CollegeDB import CollegeDB
from yims_backend.tables.SportDB import SportDB

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
    sport = relationship("SportDB", backref="matches")
    college1 = relationship("CollegeDB", foreign_keys=[college_id1])
    college2 = relationship("CollegeDB", foreign_keys=[college_id2])

    def save(self):
        session.add(self)
        session.commit()

