# zadanie 1
# telefon_number = input("Podaj swoj numer telefonu ")
# for digit in range(10):
#     digit_times_in_number = telefon_number.count(str(digit))
#     print(f"Cyfra {digit} wystepuje w Twoim numerze: {digit_times_in_number} razy")
#
# Zadanie 2 Kalkulator kredytu

capital = int(input("Na jaka kwote jest kredyt? "))
interest_rate = float(input("Jakie jest oprocentowanie (%)? "))
years = int(input("Na ile lat jest kredyt? "))
initial_fees = int(input("Jakie sa koszta poczatkowe? "))

credit_time_in_months = years * 12
monthly_paid_capital = capital / credit_time_in_months
total_paid = initial_fees
for month_number in range(1, credit_time_in_months + 1):
    capital_to_be_paid = capital - (month_number - 1) * monthly_paid_capital
    installment = (capital_to_be_paid * interest_rate / 100) / 12 + monthly_paid_capital
    total_paid += installment
    print(f"Rata w miesiacu {month_number} wyniesie {installment:.2f}")
print(f"Zaciagajac {capital} na tych warunkach splacisz z odsetkami {total_paid}")