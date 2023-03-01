class NumberParsingError(Exception):
    pass


def handle_even_number(number):
    try:
        if number % 2 != 0:
            raise NumberParsingError("To nie jest liczba parzysta!")
    except TypeError:
        raise NumberParsingError("Przekazany argument nie jest poprawna liczba")

    print(f"Dzieki! Wprowadzona liczba podzeilona przez 2 to: {number / 2}")


def run_example():
    number = input("Podaj liczbe parzysta: ")
    if number.isnumeric():
        number = int(number)

    try:
        handle_even_number(number)
    except NumberParsingError as error:
        print(f"Cos poszlo nie tak {error}")


if __name__ == "__main__":
    run_example()