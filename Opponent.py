from Character import Character
import pygame

class Opponent(Character):
    def __init__(self, x, y, image_path, speed_x=0, speed_y=0, *args, **kwargs):
        super().__init__(x, y, image_path, *args, **kwargs)
        self.speed_x = speed_x  
        self.speed_y = speed_y  
        self.is_star = False  
        self.bullets = []  
        self.can_shoot = True  

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

    def shoot(self):
        if self.can_shoot:
            bullet = self.create_bullet()
            self.bullets.append(bullet)
            self.can_shoot = False  
            print("Opponent shot a bullet!")

    def create_bullet(self):
        bullet = {
            "position": (self.rect.centerx, self.rect.bottom),  
            "direction": (0, 1),  
            "speed": 5,
            "is_active": True
        }
        return bullet

    def collide(self, player_bullet):
        if self.rect.colliderect(player_bullet.rect):
            self.is_active = False  
            player_bullet.is_active = False 
            print("Opponent hit by a bullet!")
            return True
        return False

    def render(self, screen):
        screen.blit(self.image, self.rect)

    def reset_shooting(self):
        self.can_shoot = True