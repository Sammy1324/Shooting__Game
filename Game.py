from Player import Player
from Boss import Boss
from Opponent import Opponent
from Shoot import Shoot
import pygame

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
        self.opponent = None
        self.shoots = []  
    def setup(self):
        self.player = Player(x=100, y=200, image="assets/images/Player.png", lives=3) 
        self.opponent = Opponent(x=400, y=300, image_path="assets/images/Opponent.png", lives=3, speed_x=2, speed_y=2)
        self.score = 0
        self.lives = 3
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
                        new_shoot = Shoot(x=self.player.x + self.player.width // 2, 
                                          y=self.player.y, 
                                          speed=-5, 
                                          image_path="assets/images/Shoot.png")
                        self.shoots.append(new_shoot)

    def update(self):
        if self.running:
            print("Game is updating...")
            for shoot in self.shoots[:]:
                shoot.update()
                if shoot.y < 0:  
                    self.shoots.remove(shoot)

    def render(self):
        self.screen.fill((0, 0, 0)) 
        if self.player:
            self.player.render(self.screen)  
        for shoot in self.shoots:  
            shoot.render(self.screen)
        pygame.display.flip() 

    def end_game(self):
        self.running = False
        print("Game ended!")
        self.score = 0

    def game_over(self):
        print("Game Over! You have no lives left.")
        self.running = False

    def display_status(self):
        print(f"Score: {self.score} | Lives: {self.lives}")

    def spawn_boss(self):
        print("The final boss has appeared!")
        self.opponent = Boss(x=400, y=300, image_path="assets/images/Boss.png", name="Final Boss", health=100, damage=20, special_attack="Fireball")

    def check_victory(self):
        if isinstance(self.opponent, Boss) and self.lives > 0 and not self.running:
            print("Congratulations! You defeated the final boss and won the game!")

    def main():
        game = Game()
        game.setup()
        game.start()
        pygame.quit()