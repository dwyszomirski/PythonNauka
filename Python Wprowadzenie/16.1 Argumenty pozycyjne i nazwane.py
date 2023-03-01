# Argumenty pozycyjne
# def add_two_number(first_num, second_num):
#     print(f"first_num: {first_num}")
#     print(f"second_num: {second_num}")
#     return first_num + second_num
#
# print(add_two_number(2, 5))
# print(add_two_number(5, 2))

# Taka sama definicja funkcji
def calculate_investment_value(initial_value, percentage, years):
    result = initial_value * (1 + percentage / 100) ** years
    return result

# final_value = calculate_investment_value(initial_value=1000, percentage=5, years=4)
# print(f"Po 4 latach Twoja lokata bedzie warta {final_value:.2f}")

# Mozemy przekazywac argumenty w dowolnej kolejnosci o ile je nazwiemy
final_value = calculate_investment_value(percentage=5, years=4, initial_value=1000)
print(f"Po 4 latach Twoja lokata bedzie warta {final_value:.2f}")