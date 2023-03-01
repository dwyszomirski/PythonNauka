def run_avg_speed(name, distance, time):
    avg_speed = distance / time
    print(f"{name} biega z predkoscia {avg_speed}")


def run_example():
    # Krotke tworzymy za pomoca przecinka - rozdzielacja kolejne elementy
    human_info = "Bob", "Kowalski", 35
    print(human_info)
    print(type(human_info))

    # Nawiasy sa opcjonalne - warto dodac je tworzac wprost zmienna tuple dla zwiekszenia czytelnosci
    human_info = ("Bob", "Kowalski", 35)
    print(human_info)

    # Do poszczegolnych elementow kroki odolujemy sie za pomoca indeksow
    print(human_info[0])
    print(human_info[1])
    print(human_info[2])
    print(len(human_info))
    # print(human_info[3])

    # Krotka jest immutable
    # human_info[0] = "Robert"
    # human_info.append(175)
    # human_info.sort()
    # del human_info[0]

    # Krotka moze miec tylko jeden element
    some_data = ("Mikołaj",)
    print(some_data)

    # Pusta krotke towrzymy za pomoca nawiasow albo tuple
    empty_tuple = ()
    print(empty_tuple)
    empty_tuple = tuple()
    print(empty_tuple)

    # Za pomoca tuple mozemy tez zamienic np. liste na krotke
    numbers = [0, 1, 2, 3, 4]
    tuple_numbers = tuple(numbers)
    print(tuple_numbers)

    # Po krotce mozemy literowac
    for number in tuple_numbers:
        print(number)

    # Przyklad
    run_data = ("Bob", 20, 2)
    run_avg_speed(*run_data)


if __name__ == "__main__":
    run_example()