import random


def add_random_number_to_set(numbers):
    number = random.randint(0, 10)
    numbers.add(number)
    return numbers


def add_random_number_to_frozen(numbers):
    number = random.randint(0, 10)
    return numbers.union({number})


def run_example():
    numbers = set()
    numbers = frozenset()

    while len(numbers) < 11:
        print(numbers)

        numbers = add_random_number_to_set(numbers)
        add_random_number_to_set(numbers)

        numbers = add_random_number_to_frozen(numbers)
        add_random_number_to_frozen(numbers)

    print(numbers)


def run_example_remember_results():
    numbers = set()
    numbers = frozenset()
    results = []

    while len(numbers) < 11:
        results.append(numbers)

        numbers = add_random_number_to_set(numbers)
        numbers = add_random_number_to_frozen(numbers)

    print(results)


if __name__ == "__main__":
    run_example()
    run_example_remember_results()





