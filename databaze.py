# Imports
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# DB Name
SQL_DB_URL = 'sqlite:///./databaze.db'

# Cretae engine
engine = create_engine(SQL_DB_URL, connect_args={"check_same_thread": False})

session_local = sessionmaker(autoflush=False, autocommit= False, bind=engine)

base = declarative_base()