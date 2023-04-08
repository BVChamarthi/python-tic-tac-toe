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


class tictactoe:

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

    def __init__(self):                                             # constructor
        self._board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '] # game board
        self._score_per_row = [0, 0, 0, 0, 0, 0, 0, 0]              # score is maintained individually for each row
        self._gameover = False                                      # checks whether game is over

    # d_print(player)
    # default function to print the board for console version of the game
    def d_print(self):
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]}\n---+---+---")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]}\n---+---+---")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]}")
    
    # d_print_rules(player)
    # default function to print rules for the console version of the game
    def d_print_rules(self):
        print("Python tic-tac-toe\n")
        print("To play, when it's your turn, give a number corresponding to a place on the board")
        print(" 0 | 1 | 2 \n---+---+---\n 3 | 4 | 5 \n---+---+---\n 6 | 7 | 8 \n")
    
    # reset()
    # function to reset the board
    def reset(self):
        self.board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.score_per_row = [0, 0, 0, 0, 0, 0, 0, 0]
        self.gameover = False
    
    # d_game_over(player)
    # default game_over function for console version of the game
    # displays win message of a player, game_over(1) displays player 1's message
    # game_over(2) displays player 2's message, game_over(0) shows tie message
    def d_game_over(self, player):
        if self.gameover == True:
            return
        self.d_print()
        self.gameover = True
        if player == 0:
            print("Game Over!!! It's a draw...")
            return
        print(f"Game Over!!! Player {player} won!!!")
    
    # update(player, place, game_over)
    # player can be 1 or 2, place refers to place on board, game_over is function to be called when game is over
    # game_over(player): Displays win message of player.
    def update(self, player: int, place: int, game_over) -> bool:
        self.board[place] = 'X' if player == 1 else 'O'     # place either X (player 1) or O (player 2)
        player_update = 3 - 2*player                        # convert 1 -> 1, 2 -> -1 (useful for updating score per row)
        for row in self.rows_per_place[place]:              # update scores in all rows which contain the given place
            self.score_per_row[row] += player_update
            if self.score_per_row[row] == 3 or self.score_per_row[row] == -3:
                game_over(player)
    
    # d_input(player)
    # default player input function for console version of the game
    # asks player for input, returns only when valid input is provided
    def d_input(self, player: int) -> int:
        place_str = input(f"Player {player}'s turn: ")
        if place_str.isdigit():
            place = int(place_str)
            if place < 0 or place > 8 or self.board[place] != ' ':
                return self.d_input(player)
            else:
                return place
        else:
            return self.d_input(player)
    
    # game_loop(pr_rls, pr, inp, gm_ovr)
    # game loop function for a single game
    # pr_rls(): function to print the rules of the game
    # pr(): function to print/update the board display (get board data by directly accessing it from the class)
    # inp(player): get player input
    # gm_ovr(player): display game_over msg
    def game_loop(self, pr_rls, pr, inp, gm_ovr):
        self.reset()
        pr_rls()
        i = 0
        while i < 9 and self.gameover == False:
            pr()
            self.update(1 + i%2, inp(1 + i%2), gm_ovr)
            i += 1
        gm_ovr(0)
        self.reset()
    
    # d_game_loop()
    # default game loop function for console version of the game
    def d_game_loop(self):
        self.game_loop(self.d_print_rules, self.d_print, self.d_input, self.d_game_over)

if __name__ == "__main__":
    t = tictactoe()
    t.d_game_loop()