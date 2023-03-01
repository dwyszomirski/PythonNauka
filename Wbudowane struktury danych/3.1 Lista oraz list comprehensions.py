def run_example():
    # W przykladzie wykorzystamy liste ulubionych smakow
    favourite_flavours = [
        "malinowy",
        "truskawkowy",
        "czekoladowy",
        "pistacjowy",
        "kokosowy",
    ]
    print(favourite_flavours)

    # Metoda clear usuwa wszystkie elementy z listy
    favourite_flavours.clear()
    print(favourite_flavours)

    # Metoda reverse odwraca kolejnosc elementow na liscie
    favourite_flavours.reverse()
    print(favourite_flavours)

    # Metoda count liczy liczbe wystapien (analogicznie jak na str)
    print(favourite_flavours.count("malinowy"))

    # Metoda copy tworzy kopie listy
    copy_of_flavours = favourite_flavours.copy()
    print(copy_of_flavours)

    # Metoda extend łaczy dwie listy
    new_flavours = ["orzechowy", "jagodowy"]
    favourite_flavours.extend(new_flavours)
    print(favourite_flavours)
    
    # Operator * pozwala powtorzyc liste kilkukrotnie
    new_flavours = ["orzechowy", "jagodowy"] * 4
    print(new_flavours)


if __name__ == "__main__":
    run_example()