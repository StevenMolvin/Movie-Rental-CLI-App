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
    
# Define the Rental class
class Rental(Base):
    __tablename__ = 'rentals'
    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey('movies.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    rental_date = Column(DateTime, default=datetime.now)
    return_date = Column(DateTime)
    
    movie = relationship('Movie', back_populates='rentals')
    customer = relationship('Customer', back_populates='rentals')

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
def rent_movie(session):
    title = input("Enter the movie title: ")
    
    movie = Movie(title= title)
    session.add(movie)
    session.commit()
    
    customer_name= input("Enter your name: ")
    customer = session.query(Customer).filter_by(name=customer_name).first()
    
    if customer is None:
        customer = Customer(name=customer_name)
        session.add(customer)
        session.commit()
        
    rental = Rental(movie= movie, customer= customer)
    session.add(rental)
    session.commit()
    
    print("Movie rented successfully!")

