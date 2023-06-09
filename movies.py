from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime
import click
import fire


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
    price_KES = Column(Integer)
    
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
    rented_movie = Column(String)
    customer_name = Column(String)
    rental_date = Column(DateTime, default=datetime.now)
    return_date = Column(DateTime)
    
    movie = relationship('Movie', back_populates='rentals')
    customer = relationship('Customer', back_populates='rentals')

# Create the tables in the database
Base.metadata.create_all(engine)


# Close the database session
session.close()
            


