import sys

class NineMensMorris:
    def __init__(self):
        self.board = [' ' for _ in range(24)]  # Represent the board with 24 positions
        self.player_positions = {'X': 9, 'O': 9}  # Number of remaining pieces for each player
        self.phase = 'Placement'  # Game phase: 'Placement', 'Movement', or 'Flying'
        self.current_player = 'X'  # 'X' or 'O'

    def print_board(self):
        print(f" {self.board[0]}-----------------{self.board[1]}-----------------{self.board[2]}")
        print(f" |                 |                 |")
        print(f" |    {self.board[3]}------------{self.board[4]}------------{self.board[5]}    |")
        print(f" |    |            |            |    |")
        print(f" |    |    {self.board[6]}-------{self.board[7]}-------{self.board[8]}    |    |")
        print(f" |    |    |           |    |    |    |")
        print(f"{self.board[9]}----{self.board[10]}---{self.board[11]}           {self.board[12]}---{self.board[13]}----{self.board[14]}")
        print(f" |    |    |           |    |    |    |")
        print(f" |    |    {self.board[15]}-------{self.board[16]}-------{self.board[17]}    |    |")
        print(f" |    |            |            |    |")
        print(f" |    {self.board[18]}------------{self.board[19]}------------{self.board[20]}    |")
        print(f" |                 |                 |")
        print(f" {self.board[21]}-----------------{self.board[22]}-----------------{self.board[23]}")

    def is_mill(self, position):
        # Check if a mill is formed at the given position
        row, col = position // 8, position % 8
        symbol = self.board[position]

        # Check row
        if self.board[row * 8] == symbol and self.board[row * 8 + 1] == symbol and self.board[row * 8 + 2] == symbol:
            return True
        # Check column
        if self.board[col] == symbol and self.board[col + 8] == symbol and self.board[col + 16] == symbol:
            return True
        # Check diagonals
        if (position % 2 == 0 and position % 6 != 0) or (position % 6 == 0 and position % 2 != 0):
            if self.board[9] == symbol and self.board[5] == symbol and self.board[21] == symbol:
                return True
            if self.board[3] == symbol and self.board[5] == symbol and self.board[15] == symbol:
                return True
            if self.board[3] == symbol and self.board[13] == symbol and self.board[21] == symbol:
                return True
            if self.board[15] == symbol and self.board[13] == symbol and self.board[9] == symbol:
                return True

        return False

    def is_valid_move(self, start, end):
        # Check if the move is valid based on the current game phase
        if self.phase == 'Placement':
            return self.board[end] == ' '

        elif self.phase == 'Movement':
            return self.board[start] == self.current_player and self.board[end] == ' '

        elif self.phase == 'Flying':
            return self.board[start] == self.current_player and self.board[end] == ' '

    def make_move(self, start, end):
        # Make a move and update the game state
        self.board[end] = self.board[start]
        self.board[start] = ' '

        if self.is_mill(end):
            while True:
                remove_pos = int(input("Mill formed! Choose a position to remove opponent's piece: "))
                if self.board[remove_pos] == 'O' and not self.is_mill(remove_pos):
                    self.board[remove_pos] = ' '
                    self.player_positions['O'] -= 1
                    break

    def play_game(self):
        while True:
            self.print_board()
            print(f"{self.current_player}'s turn")

            if self.phase == 'Placement':
                position = int(input("Choose an empty position to place your piece: "))
                if self.is_valid_move(None, position):
                    self.board[position] = self.current_player
                    self.player_positions[self.current_player] -= 1

            else:
                start = int(input("Choose a position to move from: "))
                end = int(input("Choose an empty position to move to: "))
                if self.is_valid_move(start, end):
                    self.make_move(start, end)

            if self.player_positions[self.current_player] == 3:
                self.phase = 'Flying'  # Move to the flying phase once each player has three pieces left

            # Switch players
            self.current_player = 'O' if self.current_player == 'X' else 'X'

            # Check for a winner
            if self.player_positions['X'] < 3:
                print("Player O wins!")
                break
            elif self.player_positions['O'] < 3:
                print("Player X wins!")
                break

if __name__ == "__main__":
    game = NineMensMorris()
    game.play_game()
