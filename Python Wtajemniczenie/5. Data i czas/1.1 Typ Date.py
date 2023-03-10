from datetime import date


def run_example():
    # Tworzenie daty za pomoca konstruktora
    march_10_2023 = date(day=10, month=3, year=2023)
    future = date(year=3053, month=3, day=10)

    print(march_10_2023)
    print(future)

    # Data musi byc poprawna (według kalendarza gregorianskiego)
    # april_31_2020 = date(year=2020, month=4, day=31)
    # future_wrong = date(year=5841, month=2, day=29)

    # Własciwosci daty
    next_birthday = date(year=2023, month=10, day=14)
    print(f"Day: {next_birthday.day}, Month: {next_birthday.month}, Year: {next_birthday.year}")

    # Obiekt jest immutable
    # next_birthday.year = 2024
    print(next_birthday)


def run_example_2():
    this_year_birthday = date(year=2023, month=10, day=14)
    next_year_birthday = date(
        year=this_year_birthday.year + 1, month=this_year_birthday.month, day=this_year_birthday.day
    )
    print(next_year_birthday)

    next_year_birthday = this_year_birthday.replace(year=this_year_birthday.year + 1)
    print(next_year_birthday)


if __name__ == "__main__":
    run_example()
    run_example_2()
