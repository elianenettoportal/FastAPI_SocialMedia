from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'
print(SQLALCHEMY_DATABASE_URL)

# establishes connects to the database
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Session talks to the SQL database 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# All models we define will extand this Base Class
Base = declarative_base()

# for every request in the API this function will create a session to the database and close it when it is done
def get_db():
    db = SessionLocal()
    print("GET_DB", db)
    try:
        yield db
    finally:
        db.close()
