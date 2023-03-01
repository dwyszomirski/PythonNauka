# Rzuczanie wyjatkami
# Exception, TypeError, KeyError, IndexError, ValueError

def run_example():
    print("Hello!")
    raise Exception("To jest bład!")
    print("To juz sie nie wypisze")


if __name__ == "__main__":
    run_example()