# Obieranie ziemniakow
# def peel_the_potatoes():
#     expected_potatoes = int(input("Ile ziemniakow chcesz na obiad? "))
#     potatoes = []
#     while len(potatoes) < expected_potatoes:
#         print("Obieram ziemniaka...")
#         print("I wrzucam go do garnka :)")
#         potatoes.append("Ziemniaki")
#     print(potatoes)
#
# # Obieranie ziemniakow = wywolanie funkcji
# # peel_the_potatoes()
# # peel_the_potatoes()
#
# def make_soup():
#     print("Jest zupa!")
#
# peel_the_potatoes()
# make_soup()

# def put_a_brick():
#     print("-", sep="", end="")
#
# # Funkcja moze wywolac inna funkcje
# def build_a_wall():
#     wall_lenght = 10
#     for brick in range(wall_lenght):
#         put_a_brick()
#     print()
# build_a_wall()
#
# def build_longer_wall():
#     wall_lenght = 30
#     for brick in range(wall_lenght):
#         put_a_brick()
#     print()
# build_a_wall()

# Funkcja moze przyjmowac parametry - widoczne wewnatrz jako zmienne
# def function_with_params(something, something_else):
#     print(something)
#     print(something_else)
#
# function_with_params(1, 4)
# function_with_params("Napis", 5)
# list_example = ["Lista", "z", "elementami"]
# dict_example = {'Klucz': 'Wartosc'}
# function_with_params(list_example, dict_example)

# Przyklad lokata
# def calculate_investment_value(initial_value, percentage, years):
#     result = initial_value * (1 + percentage / 100) ** years
#     return result
#
# def ask_for_int_value(message):
#     input_value = input(message)
#     return int(input_value)
# def run_investment_calculator():
#
#     print("Kalkulator wartosci lokaty z roczna kapitalizacja")
#
#     initial_value = ask_for_int_value("Jaka kwote wplaciles? ")
#     percentage = ask_for_int_value("Jakie jest oprocentowanie? ")
#     years = ask_for_int_value("Ile lat trwa lokata? ")
#
#     final_value = calculate_investment_value(initial_value, percentage, years)
#     print(f"Po {years} latach Twoja lokata bedzie warta {final_value:.2f}")
#
#     long_term = years * 2
#     alternative_value = calculate_investment_value(initial_value, percentage, long_term)
#     print(f"Rozwaz zostawienie lokaty na {long_term} lat - bedzie wtedy warta {alternative_value:.2f}")
#
# option = None
# while option != 'X':
#     run_investment_calculator()
#     option = input("Aby przerwac wprowadz 'X', wpisz inny znak by kontynuowac: ")

# Wiecej niz jedna wartosc
def find_best_grade(grades_by_subject):
    best_subject = None
    best_grade = 0
    for subject, grades in grades_by_subject.items():
        best_grade_from_subject = max(grades)
        if best_grade_from_subject > best_grade:
            best_grade = best_grade_from_subject
            best_subject = subject
        return best_grade, best_subject

grades_data = {
    "Historia": [5, 4, 3, 5],
    "Matematyka": [6, 4, 2, 1],
    "Fizyka": [5, 2, 1, 1]
}
# the_best_grade, subject = find_best_grade(grades_data)
# print(f"Najlepsza uzyskana ocena to {the_best_grade} z {subject}"

result = find_best_grade(grades_data)
print(result)