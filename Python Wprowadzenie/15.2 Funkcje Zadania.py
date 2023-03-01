# zadanie 1
# def ask_for_rectangle(long, width):
#     return long * width
#
# print(f"Pole prostokata o bokach 5 i 18 to {ask_for_rectangle(5, 18)}")

# zadanie 2 prędkość średnią na podstawie zadanego dystansu i czasu. V = D/T
# def average_speed(distance, time):
#     return distance / time
#
# def run_avg_speed_calculator(vehicle_name):
#     distance = float(input(f"Ile km pokonales za pomoc {vehicle_name}? "))
#     time = float(input("Ile godzin Ci to zajelo? "))
#     avg_speed = average_speed(distance, time)
#     print(f"Twoja srednia predkosc przemieszczania sie za pomoca {vehicle_name} to {avg_speed}km/h")
#
# run_avg_speed_calculator("biegu")
# run_avg_speed_calculator("roweru")
# run_avg_speed_calculator("samochodu")

# zdanie 3 budzet domowy
print("Kalkulator budzetu miesiecznego")

def load_expenditures(category_name):
    expenditures_values = []
    while True:

        expenditure = input(f"Podaj wartosc nastepnego wydatku w kategorii {category_name} albo zakoncz wpisujac 'X': ")
        if expenditure == "X":
            return expenditures_values
        expenditure_value = float(expenditure)
        expenditures_values.append(expenditure_value)

def load_expenditures_by_categories():
    expenditures = {}
    while True:
        category_name = input("Podaj kategorie wydatkow albo zakoncz wpisujac 'X': ")
        if category_name == "X":
            return expenditures
        expenditures[category_name] = load_expenditures(category_name)

def calculate_total_expenditures(expenditures):
    result = 0
    for category_expenditures in expenditures.values():
        result += sum(category_expenditures)
    return result

def calculate_expenditures_percentages(expenditures, total_expenditures):
    percentages_by_category_name = {}
    for category_name, category_expenditures in expenditures.items():
        total_category_expenditures = sum(category_expenditures)
        percentages_by_category_name[category_name] = total_category_expenditures * 100 / total_expenditures
    return percentages_by_category_name

def find_most_important_category(percentages_by_category_name):
    highest_percentage_category = None
    highest_percentage = 0
    for category, percentage in percentages_by_category_name.items():
        if percentage > highest_percentage:
            highest_percentage = percentage
            highest_percentage_category = category
        return highest_percentage_category, highest_percentage

def print_most_important_category_info(category_name, percentage):
    print(f"Najwiecej wydajesz na {category_name} - {percentage:.0f}% wszystkich wydatkow")
def print_category_info(category, percentage):
    print(f"Na {category} wydajesz {percentage:.0f}% miesiecznych wydatkow")

expenditures_by_categories = load_expenditures_by_categories()
total_expenditures = calculate_total_expenditures(expenditures_by_categories)
expenditures_percentage = calculate_expenditures_percentages(expenditures_by_categories, total_expenditures)
most_important_category, most_important_category_percentage = find_most_important_category(expenditures_percentage)

if most_important_category is not None:
    print_most_important_category_info(most_important_category, most_important_category_percentage)

for category, percentage in expenditures_percentage.items():
    print_category_info(category, percentage)