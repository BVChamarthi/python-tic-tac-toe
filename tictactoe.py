# a python module to simulate a game of tic-tac-toe


# Labelling of places on the board and rows :
#   0
#
#   1    0 | 1 | 2
#       ---+---+---
#   2    3 | 4 | 5
#       ---+---+---
#   3    6 | 7 | 8
#
#   4    5   6   7
#
# for example, row 0 contains places 0, 4 and 8


# making an array of all the rows a place is contained in
rows_per_place = (
    (0, 1, 5),          # for example, place 0 is contained in rows 0, 1 and 5
    (1, 6),             # and place 1 is contained in rows 1 and 6
    (1, 4, 7),
    (2, 5),
    (0, 2, 4, 6),
    (2, 7),
    (3, 4, 5),
    (3, 6),
    (0, 3, 7)
)

class tictactoe:
    def __init__(self):                                             # constructor
        self.board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']  # game board
        self.score_per_row = [0, 0, 0, 0, 0, 0, 0, 0]               # score is maintained individually for each row
        self.gameover = False                                       # checks whether game is over

    def print(self):                                                # function to print the board
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]}\n---+---+---")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]}\n---+---+---")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]}")
    
    def print_rules(self):
        print("Python tic-tac-toe\n")
        print("To play, when it's your turn, give a number corresponding to a place on the board")
        print(" 0 | 1 | 2 \n---+---+---\n 3 | 4 | 5 \n---+---+---\n 6 | 7 | 8 \n")
    
    def reset(self):                                                # function to reset the board
        self.board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.score_per_row = [0, 0, 0, 0, 0, 0, 0, 0]
        self.gameover = False
    
    def game_over(self, player):
        self.gameover = True
        if player == 0:
            print("Game Over!!! It's a draw...")
            return
        print(f"Game Over!!! Player {player} won!!!")
    
    def update(self, player: int, place: int) -> bool:      # player can be 1 or 2, place refers to place on board
        if place < 0 or place > 8:                          # if place number is invalid, exit the function
            return False
        if self.board[place] != ' ':                        # if a piece is already placed in the current place, exit the function
            return False
        self.board[place] = 'X' if player == 1 else 'O'     # place either X (player 1) or O (player 2)
        player_update = 3 - 2*player                # convert 1 -> 1, 2 -> -1 (useful for updating score per row)
        for row in rows_per_place[place]:           # update scores in all rows which contain the given place
            self.score_per_row[row] += player_update
            if self.score_per_row[row] == 3 or self.score_per_row[row] == -3:
                self.game_over(player)
    
    def single_turn(self, player: int):                     # simulate a single turn of the game
        self.print()
        place_str = input(f"Player {player}'s turn: ")
        while place_str.isdigit() == False or self.update(player, int(place_str)) == False:
            print("Invalid input: ", end='')
            place_str = input(f"Player {player}'s turn: ")
            if place_str.isdigit():
                place = int(place_str)
    
    def game_loop(self):
        self.reset()
        self.print_rules()
        i = 0
        while i < 9 and self.gameover == False:
            self.single_turn(1 + i%2)
            i += 1
        self.game_over(0)
        self.reset()

if __name__ == "__main__":
    t = tictactoe()
    t.game_loop()