import random


def run_example():
    bob_favourite_flavours = {"Malionwy", "Truskawkowy", "Jagodowy"}
    alice_favourite_flavours = {"Pistacjowy", "Truskawkowy", "Orzechowy"}
    print(bob_favourite_flavours)
    print(alice_favourite_flavours)

    # Suma dwoch zbiorow - smaki ktore sa ulubionymi Boba lub Alcie
    all_flavours = bob_favourite_flavours.union(alice_favourite_flavours)
    print(all_flavours)

    # Czesc wspolna - smaki, ktore lubi zarowno Bob jak i Alice
    common_flavours = bob_favourite_flavours.intersection(alice_favourite_flavours)
    print(common_flavours)

    # Roznica - smaki, ktore lubi Bob ale nie Alice
    only_bob_flavours = bob_favourite_flavours.difference(alice_favourite_flavours)
    print(only_bob_flavours)

    # Sprawdzene czy jeden zbior jest podzbiorem drugiego
    print(bob_favourite_flavours.issubset(all_flavours))

    # Usuniecie duplikatow
    numbers = [random.randint(0, 40) for _ in range(100)]
    no_duplicates = set(numbers)
    print(len(numbers))
    print(len(no_duplicates))

    # Sprawdzanie czy dana lista zawiera wszystkie podane element (nie wazne ile razy i w jakiej kolejnosci)
    digits = set([number for number in range(10)])
    print(f"Czy udalo sie wylosowac wzystkie cyfry? {digits.issubset(no_duplicates)}")


if __name__ == "__main__":
    run_example()