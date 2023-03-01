class NumberParsingError(Exception):
    pass


def ask_for_name():
    name = input("Podaj pierwsze trzy litery swojego imienia: ")
    name_len = len(name)
    if name_len < 3:
        raise ValueError("Za krotkie!")

    if name_len > 3:
        raise ValueError("Za długie!")

    print("Dziekuje :) Ja jestem python - nastepca jezyka ABC")


def run_homework():
    try:
        ask_for_name()
    except ValueError as error:
        print(f"Wprowadzone złe dane: {error}")
    else:
        print("Wszystko w porzadku, mozemy kontynuowac")
    finally:
        print("Niezaleznie od wszystkiego jestes spoko")


if __name__ == "__main__":
    run_homework()