from collections import namedtuple


Location = namedtuple("Location", ["latitude", "longitude"])


def run_example():
    location = Location(54.34, 16.54)
    print(location.latitude)
    print(location.longitude)
    print(type(location))

    location = Location(latitude=54.34, longitude=16.54)

    print(location[0])
    for coordiante in location:
        print(coordiante)


if __name__ == "__main__":
    run_example()

#
# Apple = namedtuple("Apple", ["species_name", "size", "price"])
# green_apple = Apple(species_name="Green", size="M", price=3.5)
