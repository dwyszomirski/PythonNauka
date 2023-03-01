class Teacher:

    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
        self.assigned_departments = []

    def assign_departments(self, department):
        self.assigned_departments.append(department)

    def __str__(self):
        return f"Nauczyciel przedmiotu {self.subject} - {self.name}. Uczy klasy: {self.assigned_departments}"

    # Dziedziczenie poprzez podanie nazwy klasy bazowej w nawiasach
class Tutor(Teacher):
    pass

def run_example():
    teacher = Teacher(name="Dominik", subject="Matematyka")
    teacher.assign_departments("C1")
    print(f"Nauczyciel: {teacher}")

     # Dostep do pol i metod klasy bazowej z obkietu klasy potomnej
    tutor = Tutor(name="Jakub", subject="Historia")
    print(f"Wychowawca nazywa sie {tutor.name}")
    tutor.assign_departments("A2")
    tutor.assign_departments("B1")
    print(f"Wychowawca: {tutor}")

    print(f"Nauczyciel jest typu: {type(teacher)}")
    print(f"Wychowaca jest typu: {type(tutor)}")

if __name__ == "__main__":
    run_example()