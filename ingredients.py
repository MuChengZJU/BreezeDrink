import pygame
from utils import load_image

class Ingredient:
    def __init__(self, name, image_path):
        self.name = name
        self.image = load_image(image_path)

def load_ingredients():
    ingredient_list = [
        Ingredient("Ingredient1", "assets/images/ingredient1.png"),
        Ingredient("Ingredient2", "assets/images/ingredient2.png"),
        Ingredient("Ingredient3", "assets/images/ingredient3.png"),
        Ingredient("Ingredient4", "assets/images/ingredient4.png"),
    ]
    return ingredient_list