# Zastosowanie
# 1. Sprawdzenie czy w danej kolekcji zawietaja sie konkretne elementy
# 2. Usuwanie powtorzen
# 3. Operacje matematyczne(np.suma dwoch zbiorow, czesc wspolna)

def run_example():
    # Set mozemy stworzyc przekazujac kolekcje jako argument do wbudowanego konstruktora - set
    flavours = ["Malinowy", "Truskawkowy", "Jagodowy"]
    bob_favourite_flavours = set(flavours)
    # Preferowanym sposobem wzgledem przekazania kolekcji bezposredni jest uzycie klamrowych nawiasow
    alice_favourite_flavours = {"Pistacjowy", "Truskawkowy", "Orzechowy"}
    print(bob_favourite_flavours)
    print(alice_favourite_flavours)

    # Za pomoca nawiasow klamrowych nie stworzymy pustego zbioru gdyz ten zapis jest zajesty przez słownik
    not_working_empty_set = {}
    empty_set = set()
    print(type(not_working_empty_set))
    print(type(empty_set))

    # W zbiorze elementy beda wystepowac tylko jeden raz
    alice_favourite_flavours = {"Pistacjowy", "Truskawkowy", "Orzechowy", "Orzechowy", "Orzechowy"}
    print(alice_favourite_flavours)

    # Za pomoca metody add mozemy dodac element do zbioru
    alice_favourite_flavours.add("Waniliowy")
    print(alice_favourite_flavours)

    # Remove usuwa element
    alice_favourite_flavours.remove("Pistacjowy")
    print(alice_favourite_flavours)

    # Discard dziala analogicznie do remove przy czym nie rzuca błedu gdy elementu nie ma w zbiorze
    alice_favourite_flavours.discard("Pistacjowy")
    print(alice_favourite_flavours)

    # pop wyciaga (usuwa i zwraca) element (nie wiadomo, ktory to bedzie)
    print(alice_favourite_flavours.pop())
    print(alice_favourite_flavours)

    # copy kopiuje zbior, a clear usuwa wszystkie jego elementy
    copy_of_flavours = alice_favourite_flavours.copy()
    alice_favourite_flavours.clear()
    print(alice_favourite_flavours)
    print(copy_of_flavours)

    # Metoda update dodaje elementy z jednego zbioru do drugiego
    all_flavours = alice_favourite_flavours.copy()
    all_flavours.update(bob_favourite_flavours)
    print(all_flavours)

    # Dłygosc zbioru do liczba jego elementow - tak jak w przypadku listy
    print(len(bob_favourite_flavours))

    # set nie pozwala na odwołania za pomoca indeksu - elementy nie maja kolejnosci
    # print(bob_favourite_flavours[0])

    # Elementy zbioru musza byc hashable - nie mozemy zagniezdzic jednego setu w drugim
    # set_of_set = {{"Słony karmel", "Mango"}, {"Truskawkowy", "Smietankowy"}}
    # print(set_of_set)

if __name__ == "__main__":
    run_example()