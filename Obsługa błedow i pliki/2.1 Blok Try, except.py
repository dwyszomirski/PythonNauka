# Wyjatki w programie:
# Oczekiwane - takie, ktorych wystapieniem mozemy przewidziec:
#       - Zapobiegac wystapieniu
#       - Złapanie i podjecie akcji naprwaczej
#       - Złapanie i odpowiedni komunikat dla uzytkownika
#       - Swiadome puszczenie(stack trace jako komunikat
# Zaskakujace - takie, co do ktorych nie wiemy, ze wysatpia:
#       -



def run_example():

    try:
        print("Przed rzuczeniem wyjatku")
        raise TypeError("Cos poszlo nie tak...")
        print("To sie nie wydrzay")
    except TypeError:
        print("Ale złapalismy wyjatek")

    print("I porgoram bedzie przetwarzany dalej :) ")


if __name__ == "__main__":
    run_example()