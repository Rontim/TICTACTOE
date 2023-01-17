class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def board_layout(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def spot_numbers():
        numbered_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in numbered_board:
            print('| ' + ' | '.join(row) + ' |')


    def available_spots(self):
        spots = []
        for (i, spot) in enumerate(self.board):
            if spot == ' ':
               spots.append(i)
        return spots

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    # def winner(self, square, letter):


def play(game, X , O, print_game=True):
    if print_game:
        game.spot_numbers()

    letter = 'X'
    while game.empty_squares():
        if letter == 'O':
            square = O.next_move(game)
        else:
            square = X.next_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + f" makes a move to square {square}")
                game.board_layout()
                print(" ")

            if game.current_winner:
                if print_game:
                    print(letter + " wins!")
                return letter

            letter = "O" if letter == "X" else "X"


        if print_game:
            print("it\'s a tie!")
