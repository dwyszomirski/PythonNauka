# 1
# apple_price = float(input("Ile kosztuja jabłka? "))
# orange_price = float(input("Ile kosztuja pomarancze? "))
# potato_price = float(input("Ile kosztuja ziemniaki? "))
#
# print(f"Czy jabłka sa drozsze od pomaranczy? {apple_price > orange_price}")
# print(f"Czy ziemniaki sa drozsze od jabłek? {potato_price > apple_price}")
# print(f"Czyli ziemniaki kosztuja mniej od jablek? {potato_price < apple_price}")

# 2
# produkty = input("Wprowadz liste zakupow, rozdzielajac poszczegolne elementy przecinkiem ")
# lista_produktow = produkty.split(",")
# dlugosc_listy = len(lista_produktow) > 4
# print(f"Czy uwazam, ze Twoja lista zakupow jest dluga? {dlugosc_listy}")

# 3

print("Kalkulator wartosci lokaty z roczna kapitalizacja")

initial_value_input = input("Jaka kwote wpłacilas/wplaciles? ")
initial_value = int(initial_value_input)
precenteg_input = input("Jakie jest oprocentowanie %? ")
precenteg = int(precenteg_input)
years_input = input("Ile lat trwa lokata? ")
years = int(years_input)

final_value = initial_value * (1 + precenteg / 100) ** years
capital_growth = final_value - initial_value
capital_growth_precenteg = (capital_growth / initial_value) * 100

print("Po", years, "latach Twoja lokata bedzie warta", final_value)
print(f"Czy wartosc Twojej lokaty wzrosnie w tym czasie o 10% lub wiecej? {capital_growth_precenteg >= 10}")
