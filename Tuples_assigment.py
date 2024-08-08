# Task 1: Formatting Flight Itineraries Create a Python function that takes a list of tuples as an argument. Each tuple contains information about a flight itinerary: (traveler_name, origin, destination). The function should loop through the list of itineraries and print a formatted string for each. For example, if the input is [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")], the output should be:


def format_itineraries(itineraries):
    for index, (traveler_name, origin, destination) in enumerate(itineraries, start=1):
        print(f"Itinerary {index}: {traveler_name} - From {origin} to {destination}")


# Existing Library Data
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

# Function to add a new book to the library
def add_book(library, new_book):
    if new_book not in library:
        library.append(new_book)
        print(f"Book '{new_book[0]}' by {new_book[1]} added to the library.")
    else:
        print(f"Book '{new_book[0]}' by {new_book[1]} is already in the library.")
