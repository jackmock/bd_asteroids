from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            child_1_vector = self.velocity.rotate(random_angle)
            child_2_vector = self.velocity.rotate(-random_angle)
            child_radius = self.radius - ASTEROID_MIN_RADIUS
            child_1 = Asteroid(self.position.x, self.position.y, child_radius)
            child_2 = Asteroid(self.position.x, self.position.y, child_radius)
            child_1.velocity = child_1_vector * 1.2
            child_2.velocity = child_2_vector * 1.2