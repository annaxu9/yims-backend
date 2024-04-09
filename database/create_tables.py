import sys
sys.path.append('/Users/annaxu/Desktop')

from sqlalchemy import create_engine, inspect, text
from yims_backend.models.CollegeDB import CollegeDB
from yims_backend.models.MatchDB import MatchDB
from yims_backend.models.PlayerDB import PlayerDB
from yims_backend.models.SportDB import SportDB
from yims_backend.models.UserDB import UserDB
from yims_backend.database.base import Base

engine = create_engine("mysql+mysqlconnector://root:Tiantian9!@localhost/yims")

with engine.connect() as connection:
    connection.execute(text("SET FOREIGN_KEY_CHECKS = 0;"))
    Base.metadata.drop_all(engine)
    connection.execute(text("SET FOREIGN_KEY_CHECKS = 1;"))
    connection.commit()

# Check tables after dropping
inspector = inspect(engine)
tables = inspector.get_table_names()
print("Tables after drop_all:", tables)

# Create all tables in the engine
Base.metadata.create_all(engine)

# Check tables after creating
tables = inspector.get_table_names()
print("Tables after create_all:", tables)

engine.dispose()
