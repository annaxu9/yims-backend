import sys
sys.path.append('/Users/annaxu/Desktop')

from sqlalchemy import Column, Integer, String, Float

from yims_backend.database.base import Base
from yims_backend.database.session import session



class CollegeDB(Base):
    __tablename__ = 'colleges'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))
    abbreviation = Column(String(3))
    points = Column(Float, default=0.0)

    def save(self):
        session.add(self)
        session.commit()