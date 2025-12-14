import random
import time
from player import Player, CPU
from dice import Dice

class SpecialTile:
    def __init__(self, position, effect, description):
        self.position = position
        self.effect = effect
        self.description = description

    def trigger(self, player, cpu, board_size):
        pass

class SnakeTrap(SpecialTile):
    def __init__(self, position):
        super().__init__(position, "snake_trap", "You have been bitten by a snake! Go back 3 spaces.")

    def trigger(self, player, cpu, board_size):
        player.move(-3, board_size)

class MagicPortal(SpecialTile):
    def __init__(self, position):
        super().__init__(position, "magic_portal", "You have found a magic portal! Move forward 5 spaces.")

    def trigger(self, player, cpu, board_size):
        player.move(5, board_size)

class Swamp(SpecialTile):
    def __init__(self, position):
        super().__init__(position, "swamp", "You are stuck in a swamp! Skip your next turn.")

    def trigger(self, player, cpu, board_size):
        player.skip_turn = True

class GoldenCoin(SpecialTile):
    def __init__(self, position):
        super().__init__(position, "golden_coin", "You found a golden coin, play one more time!")

    def trigger(self, player, cpu, board_size):
        player.another_turn = True

def check_collision(current_player, players, board_size):
    for other in players:
        if other is not current_player and other.position == current_player.position:
            penalty = random.randint(1, 3)
            other.move(-penalty, board_size)
            print(f"{other.name} was on the same position as {current_player.name} and has been moved {penalty} tiles back to {other.position}!")

class Game:
    def __init__(self):
        self.players = []
        self.dices = []
        self.special_tiles = []
        self.board_size = 0

    def setup(self):
        while True:
            try:
                num_players = int(input("Choose number of oppocents (1-3): "))
                if 1 <= num_players <= 4:
                    break
                else:
                    print("Please choose between 2 and 4 players.")
            except ValueError:
                print("Invalid input. Please enter a number between 2 and 4 !")

        while True:
            try:
                self.board_size = int(input("Choose board size (25-100): "))
                if 25 <= self.board_size <= 100:
                    break
                else:
                    print("Please choose a board size between 25 and 100.")
            except ValueError:
                print("Invalid input. Please enter a number between 25 and 100 !")

        self.players = [Player("You", 0)]
        self.players += [CPU(f"CPU {i+1}", 0) for i in range(num_players)]
        self.dices = [Dice() for _ in self.players]

        special_tile_count = int(self.board_size * random.uniform(0.10, 0.15))
        positions = random.sample(range(1, self.board_size - 1), special_tile_count)
        tile_classes = [SnakeTrap, MagicPortal, Swamp, GoldenCoin]

        self.special_tiles = []
        for tile_pos in positions:
            tile_cls = random.choice(tile_classes)
            self.special_tiles.append(tile_cls(tile_pos))

    def play(self):
        winner = None
        while not winner:
            for i, player_obj in enumerate(self.players):
                if player_obj.skip_turn:
                    print(f"{player_obj.name} is skipping their turn")
                    player_obj.skip_turn = False
                    continue

                extra_turn = True
                while extra_turn:
                    if i == 0:
                        input(f"{player_obj.name}, press Enter to roll the dice...")
                    else:
                        print(f"{player_obj.name} is rolling the dice...")
                        time.sleep(1)

                    roll = self.dices[i].roll()
                    player_obj.move(roll, self.board_size)
                    print(f"{player_obj.name} rolled a {roll} and is at position {player_obj.position}")
                    check_collision(player_obj, self.players, self.board_size)
                    time.sleep(1)

                    extra_turn = False
                    for tile in self.special_tiles:
                        if player_obj.position == tile.position:
                            tile.trigger(player_obj, None, self.board_size)
                            print(f"{player_obj.name} landed on a special tile: {tile.description}")
                            if player_obj.another_turn:
                                print(f"{player_obj.name} gets another turn!")
                                player_obj.another_turn = False
                                extra_turn = True

                if player_obj.position >= self.board_size:
                    print(f"Player {player_obj.name} has reached the end of the board and wins!")
                    winner = player_obj
                    break
            if winner:
                break