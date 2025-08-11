import random

class Player:
    def __init__(self, name, position, skip_turn=False, another_turn=False):
        self.name = name
        self.position = position
        self.skip_turn = skip_turn
        self.another_turn = another_turn

    def move(self, steps):
        self.position = min(board_size,max(0, self.position + steps)) # Ensure position does not exceed "Board_size" choosen by player or go below 0

    def set_position(self, pos):
        self.position = pos

    def apply_effect(self, effect):
        pass

class CPU(Player):
    def __init__(self, name, position = 0):
        super().__init__(name, position)

class Dice:
    def __init__(self, sides = 6):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)

class SpecialTile:
    def __init__(self, position, effect, description):
        self.position = position
        self.effect = effect
        self.description = description

    def trigger(self, player, cpu):
        # Apply the effect to the player
        pass

class SnakeTrap(SpecialTile):
    def __init__(self, position):
        super().__init__(position, "snake_trap", "You have been bitten by a snake! Go back 3 spaces.")

    def trigger(self, player, cpu):
        player.move(-3)

class MagicPortal(SpecialTile):
    def __init__(self, position):
        super().__init__(position, "magic_portal", "You have found a magic portal! Move forward 5 spaces.")

    def trigger(self, player, cpu):
        player.move(2)

class Swamp(SpecialTile):
    def __init__(self, position):
        super().__init__(position, "swamp", "You are stuck in a swamp! Skip your next turn.")

    def trigger(self, player, cpu):
        player.skip_turn = True

class GoldenCoin(SpecialTile):
    def __init__(self, position):
        super().__init__(position, "golden_coin", "You found a golden coin, play one more time!")

    def trigger(self, player, cpu):
        player.another_turn = True

def check_collision(current_player):
        for other in players:
            if other is not current_player and other.position == current_player.position: # if current player its not the same as other player and they are on the same position
                penalty = random.randint (1,3)
                other.move(-penalty)
                print(f"{other.name} was on the same position as {current_player.name} and has been moved {penalty} tiles back to {other.position} !")

if __name__ == '__main__':



    while True:
        try:
            num_players = int(input("Choose number of oppocents (1-3): "))
            if 2 <= num_players <= 4:
                break
            else:
                print("Please choose between 2 and 4 players.")
        except ValueError:
            print("Invalid input. Please enter a number between 2 and 4 !")

    while True:
        try:
            board_size = int(input("Choose board size (25-100): "))
            if 25 <= board_size <= 100:
                break
            else:
                print("Please choose a board size between 25 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number between 25 and 100 !")

    players = [Player("You", 0)]
    players += [Player(f"CPU {i+1}", 0) for i in range(num_players)]
    dices = [Dice() for _ in players] # Create a dice for each player

    # NUMBER OF SPECIAL TILES
    special_tile_count = int(board_size * random.uniform(0.10, 0.15)) # 10-15% of the board size
    positions = random.sample(range(1, board_size -1), special_tile_count)  # Avoid position 0 and board_size
    tile_classes = [SnakeTrap, MagicPortal, Swamp, GoldenCoin]                          # List of special tile classes

    special_tiles = []
    for tile_pos in positions:
        tile_cls = random.choice(tile_classes)
        special_tiles.append(tile_cls(tile_pos))   # Create an instance of the chosen tile class at the random position

    winner = None
    while not winner:
        for i, player_obj in enumerate(players):
            if player_obj.skip_turn:
                print(f"{player_obj.name} is skipping their turn")
                player_obj.skip_turn = False
                continue

            extra_turn = True
            while extra_turn:
                roll = dices[i].roll()
                player_obj.move(roll)
                print(f"{player_obj.name} rolled a {roll} and is at position {player_obj.position}")
                check_collision(player_obj)

                # Check if player landed on a special tile
                extra_turn = False
                for tile in special_tiles:
                    if player_obj.position == tile.position:
                        tile.trigger(player_obj, None)
                        print(f"{player_obj.name} landed on a special tile: {tile.description}")
                        if player_obj.another_turn:
                            print(f"{player_obj.name} gets another turn!")
                            player_obj.another_turn = False
                            extra_turn = True

            if player_obj.position >= board_size:
                print(f"Player {player_obj.name} has reached the end of the board and wins!")
                winner = player_obj
                break
        if winner:
            break


