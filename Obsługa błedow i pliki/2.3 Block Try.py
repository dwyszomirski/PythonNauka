def run_example():

    # try:
    #     print("Przed rzuczeniem wyjatku")
    #     raise TypeError("Cos poszło nie tak...")
    #     print("To sie nie wydarzy")
    # except ValueError as error:
    #     print("Wyjatek nie zostanie zlapany, bo nie jest tego typu")
    #
    # print("I program bedzie przetwarzany dalej :)")
    

    try:
        print("Przed rzuczeniem wyjatku")
        raise TypeError("Cos poszło nie tak...")
        print("To sie nie wydarzy")
    except Exception as error:
        print(f"Jezeli wyjatek jest klasa potomna to tez sie zlapie: {error}")

    print("I program bedzie przetwarzany dalej :)")


if __name__ == "__main__":
    run_example()