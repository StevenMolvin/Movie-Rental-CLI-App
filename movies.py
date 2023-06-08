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

# Welcome menu
def display_menu():
    print("==== Welcome to Mo's Movie Rentals ====")
    print("1. Rent a Movie")
    print("2. Return a Movie")
    print("3. List All Rented Movies")
    print("4. List All Customers")
    print("5. List Movies Due")
    print("6. Exit")
    
# Rent Movie
def rent_movie(session):
    title = input("Enter the movie title: ")
    price = input("Costs Ksh.  ")
    
    customer_name= input("Enter your name: ")
    customer = session.query(Customer).filter_by(name=customer_name).first()
    
    return_date_str = input("Enter the return date (DD-MM-YYYY HH:MM): ")
    
    try:
        return_date = datetime.strptime(return_date_str, "%d-%m-%Y %H:%M")
    except ValueError:
        print("Invalid date format. Please enter the dates in the format 'DD-MM-YYYY HH:MM'.")
        return
    
    movie = Movie(title= title, price_KES= price)
    session.add(movie)
    session.commit()
    
    if customer is None:
        customer = Customer(name=customer_name)
        session.add(customer)
        session.commit()
    
    
    rental = Rental(movie= movie, customer= customer, return_date= return_date, customer_name= customer_name, rented_movie= title)
    session.add(rental)
    session.commit()
    
    rental_id = rental.id
    
    print("")
    print("Customer name:", customer_name)
    print("")
    print("Movie:", title)
    print("")
    print("Rental ID:", rental_id)
    print("")
    print("Movie rented successfully!")
    print("")
    print("KEEP YOUR RENTAL ID SAFE! YOU WILL NEED IT WHEN RETURNING THE MOVIE!")
    print("")
    
# Return Movie
def return_movie(session):
    rental_id = input("Enter the Rental ID: ")
    rental = session.query(Rental).get(rental_id)
    
    if rental is None:
        print("Invalid ID!")
        return
    
    rental.return_date = datetime.now()
    session.commit()
    
    print("")
    print("Movie returned successfully!")
    print("")
    print("")
    
    def delete_rental(rental_id):
        rental = session.query(Rental).filter(Rental.id == rental_id).first()
    
        if rental:
            session.delete(rental)
            session.commit()
            print("Rental deleted successfully!")
        else:
            print("Rental not found!")
            print("")
    delete_rental(rental_id)
    
# List All Movies
def list_rented_movies(session):
    movies = session.query(Movie).all()
    
    print("")    
    print("============== RENTED MOVIES ==============")
    for movie in movies:
        print(f"ID: {movie.id}, Title: {movie.title}, Price: {movie.price_KES}")
        print("")
        
            
# List All Customers
def list_customers(session):
    customers = session.query(Customer).all()
    
    print("")
    print("====== CUSTOMERS LIST ======")
    for customer in customers:
        print(f"ID: {customer.id}, Name: {customer.name}")
        print("")

# List All Rentals Due
def list_rentals_due(session):
    rentals = session.query(Rental).all()
    
    print("")
    print("=================================================== MOVIES DUE ===================================================")
    for rental in rentals:
        print(f"Rental ID: {rental.id}, Movie: {rental.rented_movie}, Customer: {rental.customer_name}  Date Rented: {rental.rental_date}, Date Due: {rental.return_date}")
            
# Main program loop
while True:
    display_menu()
    choice = input("Enter you choice (1-6): ")
    
    if choice == '1':
        rent_movie(session)
    elif choice == '2':
        return_movie(session)
    elif choice == '3':
        list_rented_movies(session)
    elif choice == '4':
        list_customers(session)
    elif choice == '5':
        list_rentals_due(session)
    elif choice == '6':
        break
    else:
        print("Invalid choice. Please try again.")

# Close the database session
session.close()
            


