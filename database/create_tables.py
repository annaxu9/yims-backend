import sys
sys.path.append('/Users/annaxu/Desktop')

from sqlalchemy import create_engine
from yims_backend.tables.CollegeDB import CollegeDB
from yims_backend.tables.MatchDB import MatchDB
from yims_backend.tables.PlayerDB import PlayerDB
from yims_backend.tables.SportDB import SportDB
from yims_backend.tables.UserDB import UserDB
from yims_backend.database.base import Base

engine = create_engine("mysql+mysqlconnector://root:Tiantian9!@localhost/yims")

# Drop all tables in the engine
Base.metadata.drop_all(engine)

# Create all tables in the engine
Base.metadata.create_all(engine)