from Entity import Entity
import pygame

class Shoot(Entity):
    def __init__(self, x, y, image_path, speed):
        super().__init__(x, y, image_path)
        self.speed = speed  
        self.active = True  
    def move(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:  
            self.active = False

    def hit_target(self, target):
        if self.rect.colliderect(target.rect):  
            self.active = False
            target.hit()  

    def render(self, screen):
        if self.active:
            screen.blit(self.image, self.rect)