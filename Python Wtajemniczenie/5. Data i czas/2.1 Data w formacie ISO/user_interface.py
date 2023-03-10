from datetime import date

import books_directory
from book import Book


def _print_separator():
    print(20 * "-")
    print()


def print_available_books():
    print("Aktualne dostepne ksiazki: ")
    for book in books_directory.available_books:
        print(book)
    _print_separator()


def add_new_book():
    print("Dodawanie nowej ksiazki")
    print("Wprowadz podstawowe informacje o ksiazce")
    title = input("Tytuł: ")
    author = input("Autor: ")
    release_date_input = input("Data wydania w formacie(RRRR-MM-DD, np. 2005-05-23): ")
    release_date = date.fromisoformat(release_date_input)
    book = Book(title=title, author=author, release_date=release_date)
    books_directory.add_book(book)
    _print_separator()
    