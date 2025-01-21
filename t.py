class TicTacToe:
    def __init__(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'O'

    def print_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def is_draw(self):
        for row in self.board:
            if '' in row:
                return False
        return True

    def is_game_over(self):
        for row in self.board:
            if row[0] == row[1] == row[2] != '':
                return row[0]
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != '':
                return self.board[0][col]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            return self.board[0][2]
        if self.is_draw():
            return 'Draw'

    def ai_move(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '':
                    self.board[i][j] = 'X'
                    print(f"AI placed on ({i},{j})")
                    return

    def human_move(self):
        while True:
            try:
                row = int(input("Enter row in 0-2"))
                col = int(input("Enter col in 0-2"))
                if self.board[row][col] == '':
                    self.board[row][col] = 'O'
                    return
            except ValueError:
                pass

    def play(self):
        while True:
            self.print_board()
            result = self.is_game_over()
            if result:
                print("GAME OVER")
                if result == 'Draw':
                    print("ITS A DRAW")
                else:
                    print("Player wins")
                self.print_board()
                break
            if self.current_player == 'O':
                self.human_move()
                self.current_player = 'X'
            else:
                self.ai_move()
                self.current_player = 'O'

game = TicTacToe()
game.play()
