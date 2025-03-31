from Entity import Entity

class Character(Entity):
    def __init__(self, x, y, image, lives):
        super().__init__(x, y, image)
        self.lives = lives
        self.is_alive = lives > 0

    def move(self, direction):

        if not isinstance(direction, tuple) or len(direction) != 2:
            raise ValueError("Direction must be a tuple with two elements (dx, dy).")
        
        dx, dy = direction
        self.position[0] += dx
        self.position[1] += dy

    def shoot(self):

        projectile = {
            "position": self.position[:],  
            "direction": (0, -1),  
            "speed": 10
        }
        return projectile

    def collide(self, other_entity):
        if not isinstance(other_entity, Entity):
            raise ValueError("other_entity must be an instance of Entity.")
        
        if self.position == other_entity.position:
            self.lives -= 1 
            self.is_alive = self.lives > 0 
            return True  
        
        return False 