import random


def run_example():

    data = (input("Podaj swoje imie i nazwisko: "))
    clear_data = data.strip()
    print(f"Nazywasz sie {clear_data} - jak miło Cię poznac :) ")

    random_number = random.randint(1, 100)
    id_number = str(random_number).zfill(5)
    print(f"Twoje id to: {id_number}")

    favourite_colors = input("Jakie sa Twoje ulubione kolory? Podaj wszystkie po przecinku: ")
    if favourite_colors.lower().find("niebieski") != -1:
        print("Lubisz niebieski!")
    else:
        print("Nie lubisz niebieskiego")


if __name__ == "__main__":
    run_example()
