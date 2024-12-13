from circleshape import CircleShape
import pygame
import random
from constants import ASTEROID_MIN_RADIUS
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw (self, screen):
        pygame.draw.circle(screen,(255,255,255),(self.position.x, self.position.y), self.radius, 2)

    def update (self, dt):
        self.position += (self.velocity *dt)
    def split (self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return "this was a small asteroid and we're done"
        split_angle = random.uniform(20, 50)
        v1 = self.velocity.rotate(split_angle)        
        v2 = self.velocity.rotate((-1*split_angle)) 
        new_rad = self.radius - ASTEROID_MIN_RADIUS
        new_rock_1 = Asteroid(self.position.x,self.position.y, new_rad)
        new_rock_2 = Asteroid(self.position.x,self.position.y, new_rad)
        new_rock_1.velocity = v1 *1.2
        new_rock_2.velocity = v2 *1.2
