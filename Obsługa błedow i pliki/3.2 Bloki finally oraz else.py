#TODO try:
# ...
# except Exception as error:
# ... Zostanie wykonany tylko gdy wystapi wyjatek i go złapiemy
# else:
# ... zostanie wykonane tylko gdy NIE wystatpi wyjatek
# finally:
# ... zostanie wykonane ZAWSZE, niezaleznie od tego czy wysatpil bład

class NumberParsingError(Exception):
    pass


def handle_even_number(number_str):
    try:
        number = int(number_str)
    except ValueError:
        raise NumberParsingError("Przekazany argument nie jest poprawna liczba")

    if number % 2 != 0:
        raise NumberParsingError("To nie jest liczba parzysta")

    return number / 2


def run_example():
    number_str = input("Podaj liczbe parzysta: ")

    try:
        parsed_number = handle_even_number(number_str)
    except NumberParsingError as error:
        print(error)
    else:
        result = 100 / parsed_number
        print(f"Wynik magicznego dzialania to {result}")
    finally:
        print("Konczymy program...")


if __name__ == "__main__":
    run_example()
