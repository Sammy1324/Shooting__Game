from Character import Character

class Player(Character):
    def __init__(self, x, y, image, score=0, lives=3):
        super().__init__(x, y, image, lives)
        self.score = score
        self.lives = lives

    def move(self, direction):
        super().move(direction)

    def shoot(self):
        if self.can_shoot():
            bullet = self.create_bullet()
            bullet.set_position(self.position)
            bullet.set_direction(self.get_shooting_direction())
            self.fire_bullet(bullet)

    def take_hit(self):
        self.lives -= 1
        if self.lives <= 0:
            self.end_game()
        else:
            self.respawn()

    def end_game(self):
        print("Game Over")

    def respawn(self):
        print("Respawning...")
    