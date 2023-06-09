import click
from sqlalchemy.orm import sessionmaker
from movies import Rental, Movie, Customer, engine
from datetime import datetime
from rich.console import Console
from rich.table import Table
from tqdm import tqdm

Session = sessionmaker(bind=engine)
session = Session()
console = Console()

@click.group()
def cli():
    """CLI for interacting with the movie rental database"""
    pass

@click.command()
def rent_movie():
    """Rent a movie"""
    title = input("Enter the movie title: ")
    price = input("Costs Ksh. ")
    customer_name = input("Enter your name: ")
    return_date_str = input("Enter the return date (DD-MM-YYYY HH:MM): ")

    try:
        return_date = datetime.strptime(return_date_str, "%d-%m-%Y %H:%M")
    except ValueError:
        console.print("Invalid date format. Please enter the dates in the format 'DD-MM-YYYY HH:MM'.")
        return

    movie = Movie(title=title, price_KES=price)
    session.add(movie)
    session.commit()

    customer = session.query(Customer).filter_by(name=customer_name).first()
    if customer is None:
        customer = Customer(name=customer_name)
        session.add(customer)
        session.commit()

    rental = Rental(movie=movie, customer=customer, return_date=return_date, customer_name=customer_name, rented_movie=title)
    session.add(rental)
    session.commit()

    rental_id = rental.id

    console.print("\n[bold]Customer name:[/bold] ", customer_name)
    console.print("\n[bold]Movie:[/bold] ", title)
    console.print("\n[bold]Rental ID:[/bold] ", rental_id)
    console.print("\n[bold green]Movie rented successfully![/bold green]")
    console.print("\n[bold]KEEP YOUR RENTAL ID SAFE! YOU WILL NEED IT WHEN RETURNING THE MOVIE![/bold]\n")

@click.command()
def return_movie():
    """Return a movie"""
    rental_id = input("Enter the Rental ID: ")
    rental = session.query(Rental).get(rental_id)

    if rental is None:
        console.print("Invalid ID!")
        return

    rental.return_date = datetime.now()
    session.commit()

    console.print("\n[bold green]Movie returned successfully![/bold green]\n")

    delete_rental(rental_id)

def delete_rental(rental_id):
    rental = session.query(Rental).filter(Rental.id == rental_id).first()

    if rental:
        session.delete(rental)
        session.commit()
        console.print("Rental deleted successfully!")
    else:
        console.print("Rental not found!")

@click.command()
def list_rented_movies():
    """List all rented movies"""
    movies = session.query(Movie).all()

    table = Table(title="RENTED MOVIES")
    table.add_column("ID", justify="right", style="cyan")
    table.add_column("Title", style="yellow")
    table.add_column("Price", justify="right", style="magenta")

    for movie in tqdm(movies, desc="Loading movies"):
        table.add_row(str(movie.id), movie.title, str(movie.price_KES))

    console.print(table)

@click.command()
def list_customers():
    """List all customers"""
    customers = session.query(Customer).all()

    table = Table(title="CUSTOMERS")
    table.add_column("ID", justify="right", style="cyan")
    table.add_column("Name", style="yellow")

    for customer in tqdm(customers, desc="Loading customers"):
        table.add_row(str(customer.id), customer.name)

    console.print(table)

@click.command()
def list_rentals_due():
    """List all rentals due"""
    rentals = session.query(Rental).all()

    table = Table(title="MOVIES DUE")
    table.add_column("Rental ID", justify="right", style="cyan")
    table.add_column("Movie", style="yellow")
    table.add_column("Customer", style="green")
    table.add_column("Date Rented", style="magenta")
    table.add_column("Date Due", style="red")

    for rental in tqdm(rentals, desc="Loading rentals"):
        table.add_row(
            str(rental.id),
            rental.rented_movie,
            rental.customer_name,
            str(rental.rental_date),
            str(rental.return_date)
        )

    console.print(table)

cli.add_command(rent_movie)
cli.add_command(return_movie)
cli.add_command(list_rented_movies)
cli.add_command(list_customers)
cli.add_command(list_rentals_due)

if __name__ == "__main__":
    cli()
