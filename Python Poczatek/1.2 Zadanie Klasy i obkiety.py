class Product:
    pass

class Order:
    pass

class Apples:
    pass


class Potatoes:
    pass


if __name__ == "__main__":

    apple_a = Apples()
    apple_b = Apples()
    potatoes_a = Potatoes()
    potatoes_b = Potatoes()
    print("type(apple_a):", type(apple_a))
    print("type(apple_b):", type(apple_b))
    print("type(potatoes_a):", type(potatoes_a))
    print("type(potatoes_b):", type(potatoes_b))

    orders = [Order(), Order(), Order(), Order(), Order()]

    products = {
        "Jabłko": Product(),
        "Ziemniak": Product(),
        "Marchew": Product(),
        "Ciastka": Product()
    }
    print(products)