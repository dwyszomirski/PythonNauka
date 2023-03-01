class Student:
    pass


class  Grade:
    pass


class School:
    pass


if __name__ == "__main__":
    student_dominik = Student()

    grade_a = Grade()
    grade_f = Grade()

    my_school = School()

    # print("type(student_dominik):", type(student_dominik))
    # print("type(grade_a):", type(grade_a))
    # print("type(grade_f):", type(grade_f))
    # print("type(my_school):", type(my_school))

    all_students = [Student(), Student(), Student(), Student()]
    print(all_students)
    print(all_students[1])

    grades = {
        1: Grade(),
        2: Grade(),
        3: Grade(),
        4: Grade(),
        5: Grade(),
        6: Grade(),
    }
    print(grades)