class Player:
    def __init__(self, name, position, skip_turn=False, another_turn=False):
        self.name = name
        self.position = position
        self.skip_turn = skip_turn
        self.another_turn = another_turn

    def move(self, steps, board_size):
        self.position = min(board_size, max(0, self.position + steps))

    def set_position(self, pos):
        self.position = pos

class CPU(Player):
    def __init__(self, name, position=0):
        super().__init__(name, position)