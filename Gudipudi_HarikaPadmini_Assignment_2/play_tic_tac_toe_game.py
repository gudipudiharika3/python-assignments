import random
"""
HW: 2
Problem: Play a Tic-Tac-Toe game
Author:Gudipudi Harikapadmini
"""

class TicTacToe:

    def __init__(self):
        """Initialization of board"""
        self.board_game = []

    def setup_board(self):
        """constructing the bars on the board"""
        for i in range(3):
            row = []
            for j in range(3):
                row.append('|')
            self.board_game.append(row)

    def get_first_player(self):
        """Takes the random player to play first by using random"""
        return random.randint(0, 1)

    def fix_spot(self, row, col, player):
        """fixing given player spot on board """
        self.board_game[row][col] = player

    def is_player_win(self, player):
        """checks given player win or not"""
        n = len(self.board_game)

        # Checking columns
        for i in range(n):
            win = True
            for j in range(n):
                if self.board_game[j][i] != player:
                    win = False
                    break

            if win:
                return win

        # Checking rows
        for i in range(n):
            win = True
            for j in range(n):
                if self.board_game[i][j] != player:
                    win = False
                    break

            if win:
                return win

        # Checking diagonals
        win = True
        for i in range(n):
            if self.board_game[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.board_game[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

    def is_board_filled(self):
        """checks whether all spots occupied with player positions"""
        for row in self.board_game:
            for item in row:
                if item == '|':
                    return False
        return True

    def swap_player_turn(self, player):
        """ Swap and return the next player to play"""
        return 'X' if player == 'O' else 'O'

    def show_board(self):
        """print the board with player positions"""
        for row in self.board_game:
            for item in row:
                print(item, end=" ")
            print()

    def start(self):

        self.setup_board()
        player = 'X' if self.get_first_player() == 1 else 'O'

        while True:
            print("Player " + player + " turn")

            self.show_board()

            # user input
            row = input("Enter a row(0, 1, or 2) for player " + player + ": ")
            col = input("Enter a column(0, 1, or 2) for player " + player + ":")

            self.fix_spot(int(row), int(col), player)

            # checking current player is won or not
            if self.is_player_win(player):
                print("Player " + player + " won")
                break

            # checking the game is draw or not
            if self.is_board_filled():
                print("Match Draw")
                break

            # swapping the turn
            player = self.swap_player_turn(player)

        # final view of board
        print()
        self.show_board()


game = TicTacToe()
game.start()
