import math
# sqrt(x) = liczy pierwiastek drugiego stopnia z podanej wartosci X
# pow(x,y) = podnosi do potegi y

def calculate_c_len(a_len, b_len):
    return math.sqrt(math.pow(a_len, 2) + math.pow(b_len, 2))

a = float(input("Jaka jest długosc boku a? "))
b = float(input("Jaka jest dlugo boku b? "))
c = calculate_c_len(a, b)
print(f"Długo przeciwprostokatnej to {c:.2f}")