import random


def products_delivery():
    available_products = [
            "chleb",
            "ciastka",
            "jabłka",
            "dzem",
            "pomarancza",
            "marchew",
            "bułki",
            "ziemniaki",
            "ser",
            "mleko"
    ]
    return [available_products[random.randint(0, 9)] for _ in range(5)]


def run_homework():
    needed_products = [
            "chleb",
            "ciastka",
            "jabłka",
            "dzem",
            "pomarancza",
            "marchew",
            "bułki",
            "ziemniaki",
            "ser",
            "mleko"
    ]
    received_products = []

    while not set(needed_products) == set(received_products):
        new_products = products_delivery()
        received_products += new_products
        print(f"Otrzymano: {new_products}")
        missing_products = set(needed_products).difference(received_products)
        print(f"Brakuje nam jeszcze: {missing_products}")

    print(f"Łacznie otrzymano: {received_products}")


if __name__ == "__main__":
    run_homework()