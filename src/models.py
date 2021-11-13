import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


class User(Base):
    __tablename__= 'User'
    id= Column(Integer, primary_key=True)
    username = Column(String(250))
    firstname = Column(String(250))
    lastname = Column(String(250))
    follower = Column(Integer, ForeignKey('Follower.user_from_id'))
    post = Column(Integer, ForeignKey('Post.user_id'))
    comment = Column(Integer(), ForeignKey('Comment.author_id'))

class Follower(Base):
    __tablename__= 'Follower'
    user_from_id = Column(Integer, primary_key=True)
    user_to_id = Column(Integer, ForeignKey('User.id'))
    
    
class Post(Base):
    __tablename__='Post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    comment = Column(Integer, ForeignKey('Comment.post_id'))
    media = Column(Integer, ForeignKey('Media.post_id'))

class Comment(Base):
    __tablename__='Comment'
    id= Column(Integer, primary_key=True)
    comment_text = Column(String(250))
    author_id = Column(Integer)
    post_id = Column(Integer)

class Media(Base):
    __tablename__='Media'
    id = Column(Integer, primary_key=True)
    type = Column(Enum)
    url = Column(String(250))
    post_id = Column(Integer)





# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e