class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
        self.assigned_departments = []

    def assign_department(self, departments):
        self.assigned_departments.append(departments)

    def __str__(self):
        return f"Nauczyciel przedmiotu {self.subject} - {self.name}. Uczy klasy: {self.assigned_departments}"

class Tutor(Teacher):
    # pass

    def __init__(self, name, subject):
        print("To ja - konstruktor klasy potomnej")
        super().__init__(name, subject)
        print(f"Tutaj jest dostep do pol klasy bazowej: name={self.name}")

    # def __init__(self, name, subject):
    #     print(f"A tu jeszcze nie ma dostepu do pol klasy bazowej {self.name}")
    #     super().__init__(name, subject)

    # def __init__(self, name, subject):
    #     pass

def run_example():
    tutor = Tutor(name="Jakub", subject="Historia")

    print(f"Wychowawca nazywa się {tutor.name}")
    tutor.assign_department("B1")


if __name__ == '__main__':
    run_example()
