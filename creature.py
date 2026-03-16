import pygame
import math

class Creature:
    def __init__(self, start_x, start_y, food_x, food_y):
        self.x = start_x
        self.y = start_y
        self.food_x = food_x
        self.food_y = food_y
        self.is_alive = True
        self.radius = 6

    def move(self, outputs):
        # Normaliser le mouvement pour une vitesse constante
        max_speed = 5  # Vitesse maximale constante
        dx = (outputs[0] - 0.5) * 10  # Amplitude brute
        dy = (outputs[1] - 0.5) * 10
        
        length = math.sqrt(dx**2 + dy**2)
        if length > 0:
            # Normaliser pour vitesse constante
            self.x += (dx / length) * max_speed
            self.y += (dy / length) * max_speed

    def draw(self, screen):
        # Un petit cercle avec une bordure pour le style
        pygame.draw.circle(screen, (100, 150, 255), (int(self.x), int(self.y)), self.radius)
        pygame.draw.circle(screen, (255, 255, 255), (int(self.x), int(self.y)), self.radius, 1)

    def get_distance_to_food(self):
        return math.sqrt((self.food_x - self.x)**2 + (self.food_y - self.y)**2)