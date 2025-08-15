import pygame
from circleshape import CircleShape
from constants import *
class Shot(CircleShape):
    def __init__(self, x, y): 
        super().__init__(x, y, SHOT_RADIUS)
    
    def draw(self, surface):
        pygame.draw.circle(surface, "white", (int(self.position.x), int(self.position.y)), SHOT_RADIUS, 2)

    def update(self, dt):
        self.position += self.velocity * dt