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

    def print(self):                                                # function to print the board
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]}\n---+---+---")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]}\n---+---+---")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]}")