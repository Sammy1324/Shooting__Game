from Entity import Entity

class Shoot(Entity):
    def move(self):
        self.y -= self.speed
        if self.y < 0:
            self.active = False

    def hit_target(self, target):
        if (self.x < target.x + target.width and
            self.x + self.width > target.x and
            self.y < target.y + target.height and
            self.y + self.height > target.y):
            self.active = False
            target.hit()