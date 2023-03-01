def run_example():
    # Taka sama liste z numerami jak w poprzednim przykladnie mozemy zapisac krocej za pomoca list comprehensions
    numbers = []
    for number in range(15):
        numbers.append(number)

    numbers = [number for number in range(15)]
    print(numbers)

    # List comprehensions zawiera rowniez opcjonalna czesc if
    numbers = [number for number in range(15) if number % 2 == 0]
    print(numbers)

    # Odpowiadajaca petla for
    # numbers = []
    # for number in range(15):
    #     if number % 2 == 0:
    #         numbers.append(number)
    # print(numbers)

    # W analogiczny sposob mozemy wybrac co drugi smak
    favourite_flavours = [
        "malinowy",
        "truskawkowy",
        "czekoladowy",
        "pistacjowy",
        "kokosowy",
    ]
    flavours = [flavour for index, flavour in enumerate(favourite_flavours) if index % 2 == 0]
    print(flavours)

    # W list comprehensions mozemy uzyc rowniez pelnego wyrazenia if else
    flavours = [flavour if index % 2 == 0 else "---" for index, flavour in enumerate(favourite_flavours)]
    print(flavours)

    # Odpowiadajaca petla for
    # flavours = []
    # for index, flavour in enumerate(favourite_flavours):
    #     if index % 2 == 0:
    #         flavours.append(flavour)
    #     else:
    #         flavours.append("---")
    # print(flavours)

    # Mozemy rozwniez zagniezdzac je w sobie
    rows_and_cols = [[row for row in range(5)] for column in range(4)]
    print(rows_and_cols)

    # Odpowiadajaca petla for
    # rows_and_cols = []
    # for column in range(4):
    #     rows_and_cols.append([])
    #     for row in range (5):
    #         rows_and_cols.append(row)
    # print(rows_and_cols)


if __name__ == "__main__":
    run_example()