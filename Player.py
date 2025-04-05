from Character import Character
from Shoot import Shoot  # Import the Shoot class
import pygame

class Player(Character):
    def __init__(self, x, y, image, score=0, lives=3):
        super().__init__(x, y, image, lives)
        self.score = score
        self.lives = lives
        self.image = pygame.image.load(image)  
        self.rect = self.image.get_rect()  
        self.rect.topleft = (x, y)  
        self.bullets = []  

    def move(self, direction):
        if direction == "left":
            self.rect.x -= 5
        elif direction == "right":
            self.rect.x += 5
        elif direction == "up":
            self.rect.y -= 5
        elif direction == "down":
            self.rect.y += 5

    def render(self, screen):
        screen.blit(self.image, self.rect)
        for bullet in self.bullets:
            bullet.render(screen)

    def shoot(self):
        bullet = Shoot(x=self.rect.centerx, y=self.rect.top, image_path="bullet.png", speed=10)
        self.bullets.append(bullet)
        print("Player is shooting!")

    def update_bullets(self):
        for bullet in self.bullets:
            bullet.move()
        self.bullets = [bullet for bullet in self.bullets if bullet.active]

    def take_hit(self):
        self.lives -= 1
        if self.lives <= 0:
            self.end_game()
        else:
            self.respawn()

    def end_game(self):
        print("Game Over")

    def respawn(self):
        self.rect.topleft = (100, 200)
        print("Respawning...")