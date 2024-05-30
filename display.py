import pygame
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, BACKGROUND_COLOR, BUTTON_COLOR, BUTTON_HOVER_COLOR
from utils import load_image

class Button:
    def __init__(self, rect, color, hover_color, image_path, action):
        self.rect = pygame.Rect(rect)
        self.color = color
        self.hover_color = hover_color
        self.image = load_image(image_path)
        self.action = action
        self.hovered = False

    def draw(self, screen):
        color = self.hover_color if self.hovered else self.color
        pygame.draw.rect(screen, color, self.rect)
        image_rect = self.image.get_rect(center=self.rect.center)
        screen.blit(self.image, image_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN and self.hovered:
            self.action()

class Display:
    def __init__(self, customer, glass):
        self.customer = customer
        self.glass = glass
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.font = pygame.font.Font(None, 36)
        self.buttons = self.create_buttons()

    def create_buttons(self):
        buttons = []
        ingredients = [
            ("Ingredient1", "assets/images/ingredient1.png"),
            ("Ingredient2", "assets/images/ingredient2.png"),
            ("Ingredient3", "assets/images/ingredient3.png"),
            ("Ingredient4", "assets/images/ingredient4.png")
        ]
        for i, (ingredient, image_path) in enumerate(ingredients):
            button = Button(
                rect=(10, 100 + i * 60, 150, 50),
                color=BUTTON_COLOR,
                hover_color=BUTTON_HOVER_COLOR,
                image_path=image_path,
                action=lambda ing=ingredient: self.glass.add_ingredient(ing)
            )
            buttons.append(button)
        return buttons

    def draw(self):
        self.screen.fill(BACKGROUND_COLOR)
        self.draw_customer()
        self.draw_glass()
        for button in self.buttons:
            button.draw(self.screen)

    def draw_customer(self):
        text = self.font.render(f"Customer wants: {', '.join(self.customer.requested_drink)}", True, (0, 0, 0))
        self.screen.blit(text, (10, 10))

    def draw_glass(self):
        text = self.font.render(f"Glass contains: {', '.join(self.glass.ingredients)}", True, (0, 0, 0))
        self.screen.blit(text, (10, 50))

    def handle_event(self, event):
        for button in self.buttons:
            button.handle_event(event)