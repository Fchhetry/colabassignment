#Q no.4 implementing tic-tac-toe
import math

class TicTacToe:
    def __init__(self):
        """
        Initialize the Tic-Tac-Toe board.
        """
        self.board = [[' ' for _ in range(3)] for _ in range(3)]  # 3x3 empty board

    def print_board(self):
        """
        Display the current board state.
        """
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def is_winner(self, player):
        """
        Check if the given player has won.
        :param player: 'X' or 'O'
        :return: True if player has won, otherwise False.
        """
        for row in self.board:
            if all(cell == player for cell in row):
                return True
        for col in range(3):
            if all(self.board[row][col] == player for row in range(3)):
                return True
        if all(self.board[i][i] == player for i in range(3)) or all(self.board[i][2 - i] == player for i in range(3)):
            return True
        return False

    def is_draw(self):
        """
        Check if the game is a draw.
        :return: True if the board is full and no player has won, otherwise False.
        """
        return all(self.board[row][col] != ' ' for row in range(3) for col in range(3)) and not self.is_winner('X') and not self.is_winner('O')

    def is_terminal(self):
        """
        Check if the game has ended.
        :return: True if there is a winner or the game is a draw, otherwise False.
        """
        return self.is_winner('X') or self.is_winner('O') or self.is_draw()

    def evaluate(self):
        """
        Evaluate the board and return a score.
        :return: +10 if 'X' wins, -10 if 'O' wins, 0 otherwise.
        """
        if self.is_winner('X'):
            return 10
        elif self.is_winner('O'):
            return -10
        return 0

    def minimax(self, depth, is_maximizing, alpha=-math.inf, beta=math.inf):
        """
        Minimax algorithm with alpha-beta pruning.
        :param depth: Current depth in the game tree.
        :param is_maximizing: True if maximizing player's turn ('X'), False for minimizing player ('O').
        :param alpha: Alpha value for pruning.
        :param beta: Beta value for pruning.
        :return: Best score for the current player.
        """
        if self.is_terminal():
            return self.evaluate()

        if is_maximizing:
            best_score = -math.inf
            for row in range(3):
                for col in range(3):
                    if self.board[row][col] == ' ':
                        self.board[row][col] = 'X'
                        score = self.minimax(depth + 1, False, alpha, beta)
                        self.board[row][col] = ' '
                        best_score = max(best_score, score)
                        alpha = max(alpha, best_score)
                        if beta <= alpha:
                            break
            return best_score
        else:
            best_score = math.inf
            for row in range(3):
                for col in range(3):
                    if self.board[row][col] == ' ':
                        self.board[row][col] = 'O'
                        score = self.minimax(depth + 1, True, alpha, beta)
                        self.board[row][col] = ' '
                        best_score = min(best_score, score)
                        beta = min(beta, best_score)
                        if beta <= alpha:
                            break
            return best_score

    def find_best_move(self, is_maximizing):
        """
        Find the best move for the current player.
        :param is_maximizing: True if maximizing player's turn ('X'), False for minimizing player ('O').
        :return: Tuple (row, col) representing the best move.
        """
        best_score = -math.inf if is_maximizing else math.inf
        best_move = None

        for row in range(3):
            for col in range(3):
                if self.board[row][col] == ' ':
                    self.board[row][col] = 'X' if is_maximizing else 'O'
                    score = self.minimax(0, not is_maximizing)
                    self.board[row][col] = ' '
                    if is_maximizing and score > best_score:
                        best_score = score
                        best_move = (row, col)
                    elif not is_maximizing and score < best_score:
                        best_score = score
                        best_move = (row, col)

        return best_move

    def play_game(self):
        """
        Play the Tic-Tac-Toe game between human and AI.
        """
        current_player = 'X'
        while not self.is_terminal():
            self.print_board()
            if current_player == 'X':
                print("AI's turn (X):")
                row, col = self.find_best_move(True)
            else:
                print("Your turn (O):")
                row, col = map(int, input("Enter row and column (0-2): ").split())

            if self.board[row][col] == ' ':
                self.board[row][col] = current_player
                current_player = 'O' if current_player == 'X' else 'X'
            else:
                print("Invalid move. Try again.")

        self.print_board()
        if self.is_winner('X'):
            print("AI (X) wins!")
        elif self.is_winner('O'):
            print("You (O) win!")
        else:
            print("It's a draw!")

# Example usage
if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()
