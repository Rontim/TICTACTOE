board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

current_player = "X"
winner = None
game_play = True


# The game board

def board_layout(brd):
    print("| " + brd[0] + " | " + brd[1] + " | " + brd[2] + " |")

    print("| " + brd[3] + " | " + brd[4] + " | " + brd[5] + " |")

    print("| " + brd[6] + " | " + brd[7] + " | " + brd[8] + " |")


# Asking for the players input

def playersInput(brd):
    play = int(input("Enter a number 1-9 to choose your position: "))

    # Setting the player on a empty box represented by a dash

    if 1 <= play <= 9 and brd[play - 1] == "-":
        brd[play - 1] = current_player

    else:
        print("this spot is already checked")


# checking for a win or a tie
#   -> check the columns
#   -> check the rows
#   -> and the diagonals
#
# "<--- The global key word ensures that the variable change
#    within the given scope is reflected across the entire code --->"


def check_column(brd):
    global winner
    if brd[0] == brd[1] == brd[2] and brd[1] != "-":
        winner = brd[0]
        return True

    elif brd[3] == brd[4] == brd[5] and brd[3] != "-":
        winner = brd[3]
        return True

    elif brd[6] == brd[7] == brd[8] and brd[6] != "-":
        winner = brd[6]
        return True


def check_row(brd):
    global winner
    if brd[0] == brd[3] == brd[6] and brd[0] != "-":
        winner = brd[0]
        return True

    elif brd[1] == brd[4] == brd[7] and brd[1] != "-":
        winner = brd[1]
        return True

    elif brd[2] == brd[5] == brd[8] and brd[2] != "-":
        winner = brd[2]
        return True


def check_diagonal(brd):
    global winner
    if brd[0] == brd[4] == brd[8] and brd[0] != "-":
        winner = brd[0]
        return True

    elif brd[2] == brd[4] == brd[6] and brd[2] != "-":
        winner = brd[2]
        return True


def is_atie(brd):
    global game_play
    if "-" not in brd and not (check_diagonal(brd) or check_column(brd) or check_row(brd)):
        board_layout(brd)
        print("Its a draw!")
        game_play = False


# Switching the  players (X and O)

def switchPlayer():
    global current_player
    if current_player == "X":
        current_player = "O"

    else:
        current_player = "X"


# This function focuses mostly on the status of
# the game_play bool variable and also if the is a winner
def win():
    global game_play
    if check_diagonal(board) or check_column(board) or check_row(board):
        board_layout(board)
        print(f"The winner if {winner}")
        game_play = False


#  This while loop is acts as the game runner for thi
#  game by looping through the functions

while game_play:
    board_layout(board)
    playersInput(board)
    win()
    is_atie(board)
    switchPlayer()
