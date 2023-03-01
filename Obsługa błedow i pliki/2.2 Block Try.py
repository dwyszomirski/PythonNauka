def run_example():

    try:
        print("Przed rzuczeniem wyjatku")
        raise TypeError("Cos poszło nie tak...")
        print("To sie nie wydarzy")
    except TypeError as error:
        print(f"Wyjatek zawiera informacje: {error}")

    print("I program bedzie przetwarzany dalej :)")


if __name__ == "__main__":
    run_example()