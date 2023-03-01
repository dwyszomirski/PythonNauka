class Product:

    def __init__(self, name, category_name, unit_price):
        self.name = name
        self.category_name = category_name
        self.unit_price = unit_price

    def __str__(self):
        return f"Nazwa: {self.name} | Kategoria: {self.category_name} | Cena: {self.unit_price} PLN/szt"

class ExpiringProduct(Product):

    def __init__(self, name, category_name, unit_price, year_of_production, years_of_validity):
        super().__init__(name, category_name, unit_price)
        self.year_of_production = year_of_production
        self.years_of_validity = years_of_validity

    def does_expire(self, current_year):
        return current_year > self.year_of_production + self.years_of_validity

def run_example():

    cookies = ExpiringProduct(
        name="Ciasteczka czekoladowe",
        category_name="Jedzenie",
        unit_price=4,
        year_of_production=2020,
        years_of_validity=2
    )
    print(cookies.does_expire(2020))
    print(cookies.does_expire(2023))
    print(cookies)

if __name__ == "__main__":
    run_example()