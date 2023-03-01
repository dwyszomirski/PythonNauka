def run_example():
    # zadanie 1
    numbers1 = [number for number in range(1, 30) if number % 3 == 0]
    print(numbers1)

    numbers2 = [number for number in range(1, 30) if number % 5 == 0]
    print(numbers2)

    numbers1.extend(numbers2)
    print(numbers1)

    # zadanie 2
    print("Jakie sa Twoje ulubione sporty?")

    favourite_sports = []
    while True:
        sport = input("Podaj kolejny lub zakoncz wpisujac 'X': ")
        if sport == "X":
            break
        favourite_sports.append(sport)

    print(favourite_sports[1::2])


if __name__ == "__main__":
    run_example()