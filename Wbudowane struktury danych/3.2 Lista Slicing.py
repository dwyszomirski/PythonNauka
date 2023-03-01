def run_example():
    # W przykladzie ze slicigniem najwygodniej bedzie nam uzyc listy z elementami o wartosciach kolejnych indeksow
    numbers = []
    for number in range(15):
        numbers.append(number)
    print(numbers)

    # Podajac pojedyczna wartosc mozemy uciac liste z jednej lub drugiej strony
    print(numbers[:4])
    print(numbers[4:])

    # Poniewaz slicing zawsze zwraca nowa liste, nie podajac zadnej liczby mozemy uzyskac pelna kopie
    copy_of_numbers = numbers[:]
    print(copy_of_numbers)

    # Podajac dwie wartosci wycinamy liste z podanego przedzialu
    print(numbers[4:10])

    # Mozemy podac rowniez trzecia wartosc, ktora oznacza co ktory element chcemy wybrac
    # W tym przypadku co trzeci element pomiedzy czwartym indeksem (włacznie) a 14 (bez 14)
    print(numbers[4:14:3])

    # Powyzsze mozemy rowniez zastosowac dla ujemnych indeksow, jednak taki zapis jest juz dosc skomplikowany
    print(numbers[2:-4:3])

    # Jezeli pominiemy liczbe to bedzie wykorzystana wartosc domyslna (start = 0, koniec = długosc, skok = 1)
    print(numbers[2::3])


if __name__ == "__main__":
    run_example()