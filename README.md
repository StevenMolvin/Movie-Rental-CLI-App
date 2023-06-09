# Movie-Rental-Database
    A simple Command Line Interface which allows a user to rent films, return them and a few other
    functionalities.This is achieved by implementing python fundamentals and SQLAlchemy to create 
    and interact with the database.

# TECHNOLOGY:
    Python and SQLAlchemy

# SETUP AND INSTALLATION

    -Clone the repository from Github:
        1. Run ($ git clone git@github.com:StevenMolvin/Movie-Rental-Database.git) in your desired
           directory on your terminal.
        2. Navigate into the directory created.
    -To run the code, you will need to have python installed(Skip this step if you have Python):
        https://www.python.org/downloads/ then acquire the version that is compatible with your OS.
        or via the terminal: 
        a) MacOS
            1. $ brew update && brew upgrade
            2. $ brew install python3.11
        
        b)Linux/ Ubuntu
            1. $ sudo apt-get update && sudo apt-get upgrade
            2. $ sudo apt-get install python3.11

    -Install SQLAlchemy(Skip this step if you already have it):
        Open your terminal and run:
            1. $ pip install SQLAlchemy or
            2. $ pip3 install SQLAlchemy or
            3. $ python3 -m pip install sqlalchemy
    
    -Install dependencies:
        Open your terminal, navigate to your remote repository directory and run:
            $ pipenv install
            $ pip install click
            $ pip install rich
            $ pip install tqdm

    -Run "python3 cli.py" or "python cli.py" depending on your python version, followed by :
            1. rent-movie: to rent a movie
            2. return-movie: to return a rented movie
            3. list-rented-movies: to view the rented movies table
            4. list-customers: to view the customers table
            5. list-rentals-due: to view the rentals table
        
        for example: $ python3 cli.py list-rentals-due or $ python cli.py list-rentals-due 

    -Rent any movie ever released!, Return it!, Check out a list of movies rented out!, Check out a 
    list of customers! View a list of movies rented out, by who, when, and when they are due!

# AUTHOR

Stephen Mogusu

# CONTRIBUTION GUIDELINES
    -Fork the project
    -Create a new branch ($ git checkout -b <branch_name>)
    
# Changelog
    -All notable changes to this project will be documented in this file.
    
## Initial Release
    [1.0.0] June 2021

# LICENSE
MIT License 
Copyright (c) 2023 Stephen Mogusu
    
    
