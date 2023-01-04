'''
        This is the schema model of the SQL Alchemy
        it will create a table in the base model
        it will define the types and rules config for the tables and columns
'''
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from .database import Base

class Post(Base):
    __tablename__= 'posts'

    id        = Column(Integer, primary_key=True, nullable=False)
    title     = Column(String, nullable=False)
    content   = Column(String, nullable=False)
    published = Column(Boolean, server_default='TRUE', nullable=False)
    created_at= Column(TIMESTAMP(timezone=True),nullable=False, server_default=text('now()'))
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    
    # SQLALchemy relationship one-to-many- returns the class of another model
    owner = relationship("User")

class User(Base):
    __tablename__ = "users"

    id         = Column(Integer, primary_key=True, nullable=False)
    email      = Column(String, nullable=False, unique=True)
    password   = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False, server_default=text('now()'))

# Composite Keys  - primary key represented by multiple columns, no register duplicated will be allowed
class Vote(Base):
    __tablename__ = "votes"

    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    post_id = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"), primary_key=True)