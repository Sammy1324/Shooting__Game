from Opponent import Opponent
import pygame

class Boss(Opponent):
    def __init__(self, x, y, image_path, name, health, damage, special_attack):
        super().__init__(name, health, damage)
        self.special_attack = special_attack
        self.image = pygame.image.load(image_path)  # Load the boss image
        self.rect = self.image.get_rect()  # Get the rectangle for positioning
        self.rect.topleft = (x, y)  # Set the initial position

    def take_damage(self, amount):
        reduced_damage = amount * 0.5
        self.health -= reduced_damage
        print(f"{self.name} took {reduced_damage} damage! Remaining health: {self.health}")

    def attack(self):
        print(f"{self.name} attacks with {self.damage} damage!")

    def use_special_attack(self):
        print(f"{self.name} uses a special attack: {self.special_attack}!")

    def move(self, dx, dy):
        # Move the boss based on the given direction
        self.rect.x += dx
        self.rect.y += dy

    def render(self, screen):
        # Draw the boss on the screen
        screen.blit(self.image, self.rect)

    def collide(self, other_entity):
        # Check for collision with another entity
        if self.rect.colliderect(other_entity.rect):  # Use pygame's collision detection
            print(f"{self.name} collided with {other_entity}")
            return True
        return False