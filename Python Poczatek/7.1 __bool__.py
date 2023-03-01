class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.promoted = False

    def __bool__(self):
        return self.promoted

def run_example():
    student = Student(first_name="Dominik", last_name="Bombelowski")
    print(bool(student))

    student.promoted = True
    print(bool(student))

    if student:
        print("If Student")

    student.promoted = False
    if student:
        print("if student")

if __name__ == "__main__":
    run_example()