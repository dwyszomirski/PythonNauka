def handle_even_number(number):

    if number % 2 != 0:
        raise ValueError("To nie jest liczba parzysta!")

    print(f"Dzieki! Wprowadzona liczba podzielona przez 2 to: {number / 2}")


def run_example():
    number = input("Podaj liczbe parzysta: ")
    if number.isnumeric(): # sprawdzanie czy string jest podobny do liczby
        number = int(number)

    try:
        handle_even_number(number)
    except TypeError as error:
        print(f"Cos nie tak z typem: {error}")
    except ValueError as error:
        print(f"Zła wartosc: {error}")


if __name__ == "__main__":
    run_example()
