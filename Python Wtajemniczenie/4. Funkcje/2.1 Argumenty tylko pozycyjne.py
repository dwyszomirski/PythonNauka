# TODO Przyjecie argumentow pozycyjnie oraz dowolnych argumentow przez **kwargs
# TODO Nazwa argumentu nie ma znaczenia
# TODO Nazwa funkcji jednoznacznie wskazuje na wymaganie konkretnego argumentu


def example_fun(pos_1, pos_2, /, *, key_3):
    print(pos_1, pos_2, key_3)


def run_example():
    # example_fun(5, 10, 15)
    example_fun(5, 10, key_3=15)
    # example_fun(5, pos_or_key_2=10, pos_or_key_3=15)
    # example_fun(pos_or_key_1=5, pos_or_key_2=10, pos_or_key_3=15)


if __name__ == "__main__":
    run_example()