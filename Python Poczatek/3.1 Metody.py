class Student:
    def __init__(self, name):
        self.name = name

    def print_something(self):
        print("To ja - metoda studenta!")

    def print_self(self):
        print("Czym jest self?: ", self)
        print("Jest tutaj dostep do name:", self.name)

    def do_all_work(self):
        print("Teraz to sie napracuje")
        self.do_pice_of_work()
        self.do_pice_of_work()
        self.do_pice_of_work()
        print("Koniec :)")

    def do_pice_of_work(self):
        print("Robota....")


def run_example():
    student = Student(name="Dominik")
    # Wywołanie metody
    student.print_something()

    # Pierwszy przekazany niejwanie arguemnt, zwaiera referencje na aktualny obkiet
    student.print_self()

    # Metoda moze wywołac inna metode
    student.do_all_work()

if __name__ == "__main__":
    run_example()