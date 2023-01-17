import math
import  random

class Player:
    def __init__(self, letter):
        self.letter = letter

    def next_move(self, game):
        pass


class computer_player(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def next_move(self, game):
        square = random.choice(game.available_spots())
        return square


class real_player(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def next_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move(0-9): ')
            try:
                val = int(square)
                if val not in game.available_spots():
                    raise ValueError
            except ValueError:
                print('Invalid square. Try again.')

        return val
