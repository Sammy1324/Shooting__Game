from Character import Character

class Opponent(Character):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_star = False  

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def shoot(self):
        if self.can_shoot:
            bullet = self.create_bullet()
            self.bullets.append(bullet)
            self.can_shoot = False

    def collide(self, player_bullet):
        if self.rect.colliderect(player_bullet.rect):
            self.score += 1
            self.is_active = False
            player_bullet.is_active = False