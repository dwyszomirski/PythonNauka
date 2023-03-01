# Wartosc domysla
# def best_grades(grades, best_grades_number=1):
#     grades.sort(reverse=True)
#     if best_grades_number < len(grades):
#         return grades[:best_grades_number]
#     print("Nie mozna zwrocic wiecej ocen niz jest na liscie. Zostana zwrocone wszystkie...")
#     return grades
#
# math_grades = [1, 3, 4, 4, 5, 1, 5]
# print(best_grades(math_grades))
# print(best_grades(math_grades, best_grades_number=4))

def write_final_grade(subject_grades, final_grades=None):
    if final_grades is None:
        final_grades = []
    grades_avg = sum(subject_grades) / len(subject_grades)
    final_grades.append(float(grades_avg))
    return final_grades

john_math_grades = [3, 4, 5, 2, 5]
john_physic_grades = [1, 2, 1, 5, 5]
john_final_grades = write_final_grade(subject_grades=john_math_grades)
john_final_grades = write_final_grade(subject_grades=john_physic_grades, final_grades=john_final_grades)
print(f"Oceny Johna: {john_final_grades}")

bob_math_grades = [1, 2, 2, 6, 5]
bob_physic_grades = [2, 2, 5, 5, 6, 4]
bob_final_grades = write_final_grade(subject_grades=bob_math_grades)
bob_final_grades = write_final_grade(subject_grades=bob_physic_grades, final_grades=bob_final_grades)
print(f"Oceny Boba: {bob_final_grades}")