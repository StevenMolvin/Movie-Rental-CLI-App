#!/usr/bin/env python3

from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

if __name__ == '__main__':
    # Create the database engine
    engine = create_engine('sqlite:///movie_rental.db')
    Base = declarative_base()
    Session = sessionmaker(bind=engine)
    session = Session()
    
# Define the Movie class
class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    length = Column(String)
    release_date = Column(DateTime)
    