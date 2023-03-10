import user_interface, books_directory


def run_example():
    user_interface.print_available_books()
    user_interface.add_new_book()
    print("Data dodania: ", books_directory.available_books[-1].added_at_date)


if __name__ == "__main__":
    run_example()
