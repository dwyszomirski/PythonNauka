class Student:

    # Zadaniem konstruktora jest zdefiniowanie i zainicjalizowac stan obiektu
    def __init__(self):
        self.first_name = "Dominik"
        self.second_name = "Bombelowski"
        self.age = 23

def run_example():
    student = Student()
    # Do stanu obkietu mamy dostep - mozemy go odczytac
    print(student.first_name)
    print(student.second_name)
    print(student.age)

    # Stan Obkietu mozemy rowniez modyfikowac
    student.first_name = "Karola"
    student.second_name = "Bombelowska"
    student.age = 18
    print(student.first_name)
    print(student.second_name)
    print(student.age)


if __name__ == "__main__":
    run_example()