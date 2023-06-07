from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

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
    rentals = relationship('Rental', back_populates='movie')

# Define the Customer class
class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    rentals = relationship('Rental', back_populates='customer')

# Create the tables in the database
Base.metadata.create_all(engine)

# Welcome menu
def display_menu():
    print("==== Welcome Mo's Movie Rental ====")
    print("1. Rent a Movie")
    print("2. Return a Movie")
    print("3. List All Movies")
    print("4. List All Customers")
    print("5. Exit")
    
# Rent Movie
def rent_movie():
    title = input("Enter the movie title: ")

