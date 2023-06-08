from movies import display_menu, rent_movie, return_movie, list_rented_movies, list_customers
def program():
# Main program loop
    while True:
        display_menu()
        choice = input("Enter you choice (1-5): ")
    
        if choice == '1':
            rent_movie(session)
        elif choice == '2':
            return_movie(session)
        elif choice == '3':
            list_rented_movies(session)
        elif choice == '4':
            list_customers(session)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")