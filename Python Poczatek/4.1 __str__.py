import random

class Student:
    def __init__(self, first_name, last_name):
        self.fist_name = first_name
        self.last_name = last_name
        self.promoted = False

    def __str__(self):
        return f"Student: {self.fist_name} {self.last_name}, promoted:{self.promoted}"

class School:

    def __init__(self, name, students):
        self.name = name
        self.students = students

    def __str__(self):
        students = ""
        for student in self.students:
            students += "\n"
            students += str(student)

        return f"School: {self.name}, with {len(self.students)} students: {students}"

def create_school_with_students(school_name):
        number_of_students = random.randint(1, 20)
        students = []
        for student_number in range(number_of_students):
            first_name = f"Student {student_number}"
            last_name = "Smith"
            students.append(Student(first_name, last_name))

        school = School(school_name, students)
        return school

def run_example():
        school = create_school_with_students("Hogwart")
        print(school)

if __name__ == "__main__":
    run_example()