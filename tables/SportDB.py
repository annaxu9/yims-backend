import sys
sys.path.append('/Users/annaxu/Desktop')

from sqlalchemy import Column, Integer, String

from yims_backend.database.base import Base
from yims_backend.database.session import session


class SportDB(Base):
    __tablename__ = 'sports'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))
    points_for_win = Column(Integer)
    season = Column(String(20))
    icon = Column(String(20))
    
    def save(self):
        session.add(self)
        session.commit()