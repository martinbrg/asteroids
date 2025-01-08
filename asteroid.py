import random

from circleshape import *
from constants import ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen, color):
        #last param is line width, constant 2
        pygame.draw.circle(screen, color, self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)


    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS: #small
            return
        else:
            random_angle = random.uniform(20, 50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            
            first = Asteroid(self.position.x, self.position.y, new_radius)
            second = Asteroid(self.position.x, self.position.y, new_radius)

          
            first.velocity = self.velocity.copy()
            first.velocity = first.velocity.rotate(random_angle)
            first.velocity *= 1.2
            second.velocity = self.velocity.copy()
            second.velocity = second.velocity.rotate(-random_angle)
            second.velocity *= 1.2