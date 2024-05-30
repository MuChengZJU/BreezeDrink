import pygame
from customer import Customer
from glass import Glass
from display import Display
from constants import FPS

class Game:
    def __init__(self):
        self.customer = Customer()
        self.glass = Glass()
        self.display = Display(self.customer, self.glass)
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(FPS)
        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            self.display.handle_event(event)

    def update(self):
        # 更新游戏状态逻辑
        pass

    def render(self):
        self.display.draw()
        pygame.display.flip()