import random

class School:
    def __init__(self, name, students):
        self.name = name
        self.students = students

    def print_self(self):
        print(f"School: {self.name}, with {len(self.students)} students:")
        for student in self.students:
            student.print_self()
class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.second_name = last_name
        self.promoted = False
        self.final_grades = []

    def promote(self):
        self.promoted = True

    def add_final_grade(self, grade):
        self.final_grades.append(grade)
        if grade == 1:
            self.promoted = False
    def print_self(self):
        print(f"Student: {self.first_name} {self.second_name}, promoted: {self.promoted}, Final grades: {self.final_grades}")


# Funkcja moze zwracac obiekty
def create_school_with_student(school_name):
    number_of_students = random.randint(1, 20)
    students = []
    for student_number in range(number_of_students):
        first_name = f"Student{student_number}"
        last_name = "Smith"
        students.append(Student(first_name, last_name))

    school = School(school_name, students)
    return school


def run_example():

    school = create_school_with_student("Hogwart")
    for student in school.students:
        student.promote()
    school.print_self()
    print("=" * 20)

    for student in school.students:
        final_grade = random.randint(1, 3)
        student.add_final_grade(final_grade)
    school.print_self()


if __name__ == "__main__":
    run_example()
