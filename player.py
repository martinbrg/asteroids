from circleshape import *
from constants import *
from shot import *

class Player(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.timer = 0


    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        #dt is delta time, return value from clock.tick
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rotate(dt*-1)
        if keys[pygame.K_RIGHT]:
            self.rotate(dt)
        if keys[pygame.K_UP]:
            self.move(dt)
        if keys[pygame.K_DOWN]:
            self.move(dt*-1)
        if keys[pygame.K_SPACE]:
            self.shoot(self.rotation)
            self.timer -= dt


    def draw(self, screen, color):
        #last param is line width, constant 2
        pygame.draw.polygon(screen, color, self.triangle(), 2)

        return super().draw(screen)
    

    def shoot(self, direction):
        if not self.timer > 0:
            shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
            shot.velocity = pygame.Vector2(0, 1)
            shot.velocity = shot.velocity.rotate(direction)
            shot.velocity *= PLAYER_SHOOT_SPEED

            self.timer = PLAYER_SHOOT_COOLDOWN


