from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create an engine that connects to the MySQL database
engine = create_engine("mysql+mysqlconnector://root:Tiantian9!@localhost/yims")

# Create a sessionmaker factory bound to the engine
Session = sessionmaker(bind=engine)

# Create a new session
session = Session()