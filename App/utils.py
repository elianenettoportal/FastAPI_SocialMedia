'''
Utils file used for any common action in the API
'''
from passlib.context import CryptContext
from .database import engine
from . import models

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash(password: str):
    return pwd_context.hash(password)


def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# Note: SQLAlchemy will see if tables exists, if not it creates
def database_exists():
    try:
        print("WILL CREATE")
        models.Base.metadata.create_all(bind=engine) 
        database='CREATED'  
    except:
        print("Already exists")
        database='EXISTS'
    
    return database