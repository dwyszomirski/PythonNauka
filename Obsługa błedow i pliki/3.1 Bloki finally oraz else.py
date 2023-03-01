# TODO try:
#     ...
#     ...
#     ...
# TODO except Exception as error:
#     ... Zostanie wykonane tylko gdy wystatpi wyjatek i go złapiemy
# TODO finally:
#     ... Zostanie, wykonane ZAWSZE, niezaleznie od tego czy wystapil bład

class NumberParsingError(Exception):
    pass


def handle_even_number(number_str):
    try:
        number = int(number_str)
    except ValueError:
        raise NumberParsingError("Przekazany argument nie jest poprawna liczba")

    if number % 2 != 0:
        raise NumberParsingError("To nie jest liczba parzysta")

    print(f"Dzieki! Wprowadzona liczba podzielona przez 2 to: {number / 2}")


def run_example():
    number_str = input("Podaj liczbe parzysta: ")

    # try:
    #     handle_even_number(number_str)
    # finally:
    #     print("Błedu nie złapiemy ale wykonamy to zawsze")

    try:
        handle_even_number(number_str)
    except NumberParsingError as error:
        print(error)
        raise error
    finally:
        print("Błedu nie złapiemy ale wykonamy to zawsze")


if __name__ == "__main__":
    run_example()