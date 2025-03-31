from Player import Player
from Boss import Boss

class Game():
    def __init__(self):
        self.score = 0
        self.player = None
        self.opponent = None
        self.is_running = False

    def setup(self):
        self.player = Player(x = 100, y = 200, image = any, lives=3)
        self.opponent = None
        self.lives = 3
        self.score = 0
        self.is_running = False
        print("Game setup complete. Ready to start!")

    def start(self):
        self.is_running = True
        self.score = 0
        print("Game started!")

    def update(self):
        if self.is_running:
            print("Game is updating...")
        else:
            print("Game is not running.")

    def end_game(self):
        self.is_running = False
        print("Game ended!")
        self.score = 0

    def increase_score(self, points):
        self.score += points
        print(f"Score increased by {points}. Current score: {self.score}")

    def convert_enemy_to_star(self, enemy):
        self.increase_score(10) 
        enemy.convert_to_star()

    def take_damage(self):
        self.lives -= 1
        print(f"Lives remaining: {self.lives}")
        if self.lives <= 0:
            self.game_over()

    def game_over(self):
        print("Game Over! You have no lives left.")

    def display_status(self):
        if self.is_running:
            print(f"Score: {self.score} | Lives: {self.lives}")
        else:
            print("Game is not running. No status to display.")

    def remove_opponent(self, opponent):
        print(f"Opponent {opponent} defeated!")
        self.opponent = None
        if not self.is_boss_spawned():
            self.spawn_boss()

    def is_boss_spawned(self):
        return isinstance(self.opponent, Boss)

    def spawn_boss(self):
        print("The final boss has appeared!")
        self.opponent = Boss()

    def check_victory(self):
        if isinstance(self.opponent, Boss) and self.lives > 0 and not self.is_running:
            print("Congratulations! You defeated the final boss and won the game!")