def run_example():
    # Frozenset tworzymy za pomoca wbudowanego konstruktora - frozenset
    flavours = ["Malinowy", "Truskawkowy", "Jagodowy"]
    bob_favourite_flavours = frozenset(flavours)
    print(type(bob_favourite_flavours))

    alice_favourite_flavours = frozenset({"Pistacjowy", "Truskawkowy", "Orzechowy"})
    print(type(alice_favourite_flavours))

    # Frozenset rownies usuwa duplikaty oraz pozwala wykonac operacje matematyczne na zbiorach
    alice_favourite_flavours = frozenset({"Pistacjowy", "Truskawkowy", "Orzechowy", "Orzechowy", "Orzechowy"})
    print(alice_favourite_flavours)
    common_flavours = bob_favourite_flavours.intersection(alice_favourite_flavours)
    print(common_flavours)
    all_flavours = bob_favourite_flavours.union(alice_favourite_flavours)
    print(all_flavours)

    # Nie pozwala on natomiast na modyfikacje
    # alice_favourite_flavours.add("Waniliowy")
    # alice_favourite_flavours.remove("Pistacjowy")
    # alice_favourite_flavours.discard("Pistacjowy")
    # alice_favourite_flavours.pop()

    # Dzieki temu, ze frozenset jest immutable mozemy za jego pomoca stowrzyc zbior zbiorow
    set_of_set = {frozenset({"Karmel", "Mango"}), frozenset({"Czekoladowy", "Smietankowy"})}
    print(set_of_set)


if __name__ == "__main__":
    run_example()