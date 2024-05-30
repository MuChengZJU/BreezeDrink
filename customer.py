import random

class Customer:
    def __init__(self):
        self.requested_drink = self.request()

    def request(self):
        # 生成饮品要求逻辑
        ingredients = ["Ingredient1", "Ingredient2", "Ingredient3", "Ingredient4"]
        return random.sample(ingredients, k=2)

    def is_satisfied(self, glass):
        # 判断搅拌杯中的饮品是否满足顾客要求
        return set(self.requested_drink) == set(glass.ingredients)