class Glass:
    def __init__(self):
        self.ingredients = []

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)
        print(f"Added {ingredient}. Current ingredients: {self.ingredients}")