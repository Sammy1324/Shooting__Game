from Entity import Entity
import pygame

class Character(Entity):
    def __init__(self, x, y, image, lives):
        super().__init__(x, y, image)
        self.lives = lives
        self.is_alive = lives > 0
        self.image = pygame.image.load(image)  
        self.rect = self.image.get_rect() 
        self.rect.topleft = (x, y)  

    def move(self, direction):
        if not isinstance(direction, tuple) or len(direction) != 2:
            raise ValueError("Direction must be a tuple with two elements (dx, dy).")
        
        dx, dy = direction
        self.rect.x += dx
        self.rect.y += dy

    def shoot(self):
        projectile = {
            "position": (self.rect.centerx, self.rect.top),  
            "direction": (0, -1), 
            "speed": 10
        }
        return projectile

    def collide(self, other_entity):
        if not isinstance(other_entity, Entity):
            raise ValueError("other_entity must be an instance of Entity.")
        
        if self.rect.colliderect(other_entity.rect):  
            self.lives -= 1
            self.is_alive = self.lives > 0
            return True
        
        return False

    def render(self, screen):
        screen.blit(self.image, self.rect)