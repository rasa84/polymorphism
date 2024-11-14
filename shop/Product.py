class Product:
    def __init__(self, name, weight_kg, price):
        self.name = name
        self.weight_kg = weight_kg
        self.price = price

    def price_per_kg(self):
        return self.price / self.weight_kg

    # def __eq__(self, other):
    #     return self.price_per_kg() == other.price_per_kg()
    #
    # def __ne__(self, other):
    #     return self.price_per_kg() != other.price_per_kg()
    #
    # def __lt__(self, other):
    #     return self.price_per_kg() < other.price_per_kg()
    #
    # def __le__(self, other):
    #     return self.price_per_kg() <= other.price_per_kg()

    def __gt__(self, other):
        return self.price_per_kg() > other.price_per_kg()

    def __ge__(self, other):
        return self.price_per_kg() >= other.price_per_kg()

    def __str__(self):
        return f"Prekė: {self.name}, svoris: {self.weight_kg} kg, kaina: {self.price} eur."
