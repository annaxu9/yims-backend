import sys
sys.path.append('/Users/annaxu/Desktop')

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from yims_backend.database.base import Base
from yims_backend.database.session import session
from yims_backend.models.PlayerDB import PlayerDB

class UserDB(Base):
    __tablename__ = 'users'
    netid = Column(String(10), primary_key=True)
    firstname = Column(String(20))
    lastname = Column(String(20))
    college_id = Column(Integer, ForeignKey('colleges.id'))
    role = Column(String(10))  # role can be 'player', 'admin', 'ref', "sec", or "president"
    points = Column(Integer, default=0)

    player_entries = relationship("PlayerDB", back_populates="user")

    def save(self):
        session.add(self)
        session.commit()

