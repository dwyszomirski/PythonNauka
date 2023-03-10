# TODO "Pasuje" do niektorych algorytmow(czytelnosci)
# TODO Gorsza wydajnosc, limit wywołan

def factorial_recursive(number):
    if number == 0:
        return 1
    return number * factorial_recursive(number - 1)


# def factorial_iterative(number):
#     result = 1
#     for current_number in range(1, number + 1):
#         result *= current_number
#     return result


def run_example():
    result = factorial_recursive(5)
    # result1 = factorial_iterative(5)

    print(result)
    # print(result1)


if __name__ == "__main__":
    run_example()
