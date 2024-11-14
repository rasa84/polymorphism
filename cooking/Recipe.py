class Recipe:
    def __init__(self, name, ingredients, servings=1):
        self.name = name
        self.ingredients = ingredients
        self.servings = servings

    def __str__(self):
        output = f"Receptas: {self.name} ({self.servings} porcijos)\nIngredientai:\n"
        for ingredient, quantity in self.ingredients.items():
            output += f"\t - {ingredient}: {quantity} \n"
        return output

    def __mul__(self, factor):
        new_ingredients = {i: q * factor for i, q in self.ingredients.items()}
        return Recipe(self.name, new_ingredients, self.servings * factor)

    def __truediv__(self, divisor):
        new_ingredients = {i: q / divisor for i, q in self.ingredients.items()}
        return Recipe(self.name, new_ingredients, self.servings / divisor)