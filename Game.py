from Player import Player
from Boss import Boss
from Opponent import Opponent
from Shoot import Shoot
import pygame
#corregir para que dispare 
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Shooting Game")
        self.clock = pygame.time.Clock()
        self.running = False
        self.score = 0
        self.lives = 3
        self.player = None
        self.opponents = []
        self.shoots = []
        self.opponent_shoots = []
        self.defeated_opponents = 0

    def setup(self):
        self.player = Player(x=100, y=500, image="assets/images/Player.png", lives=3)
        self.opponents = [
            Opponent(x=400, y=100, image_path="assets/images/Opponent.png", lives=3, speed_x=2, speed_y=2)
        ]
        self.score = 0
        self.lives = 3
        self.defeated_opponents = 0
        self.running = True
        print("Game setup complete. Ready to start!")

    def start(self):
        self.running = True
        print("Game started!")
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.player:
                        self.player_shoot()

    def player_shoot(self):
        new_shoot = Shoot(
            x=self.player.x + 2, 
            y=self.player.y,
            speed=-5,
            image_path="assets/images/Bullet.png"
        )
        self.shoots.append(new_shoot)

    def update(self):
        if self.running:
            for shoot in self.shoots[:]:
                shoot.move()
                if shoot.y < 0:
                    self.shoots.remove(shoot)
                else:
                    for opponent in self.opponents[:]:
                        if opponent.collide(shoot):
                            opponent.lives -= 1
                            self.shoots.remove(shoot)
                            if opponent.lives <= 0:
                                self.opponents.remove(opponent)
                                self.defeated_opponents += 1
                                if self.defeated_opponents == 3:
                                    self.spawn_boss()

            for shoot in self.opponent_shoots[:]:
                shoot.move()
                if shoot.y > 600:
                    self.opponent_shoots.remove(shoot)
                elif self.player and self.player.take_hit():
                    self.lives -= 1
                    self.opponent_shoots.remove(shoot)
                    if self.lives <= 0:
                        self.game_over()

            for opponent in self.opponents:
                opponent.move()
                if opponent:
                    new_shoot = Shoot(
                        x=opponent.x,
                        y=opponent.y,
                        speed=5,
                        image_path="assets/images/Bullet.png"
                    )
                    self.opponent_shoots.append(new_shoot)

    def render(self):
        self.screen.fill((0, 0, 0))
        if self.player:
            self.player.render(self.screen)
        for opponent in self.opponents:
            opponent.render(self.screen)
        for shoot in self.shoots:
            shoot.render(self.screen)
        for shoot in self.opponent_shoots:
            shoot.render(self.screen)
        self.display_status()
        pygame.display.flip()

    def end_game(self):
        self.running = False
        print("Game ended!")
        self.score = 0

    def game_over(self):
        print("Game Over! You have no lives left.")
        self.running = False
        pygame.quit()

    def display_status(self):
        font = pygame.font.Font(None, 36)
        status_text = f"Score: {self.score} | Lives: {self.lives}"
        text_surface = font.render(status_text, True, (255, 255, 255))
        self.screen.blit(text_surface, (10, 10))

    def spawn_boss(self):
        print("The final boss has appeared!")
        self.opponents = [
            Boss(x=400, y=100, image_path="assets/images/Boss.png", name="Final Boss", health=100, damage=20, special_attack="Fireball")
        ]

    def main():
        game = Game()
        game.setup()
        game.start()
        pygame.quit()