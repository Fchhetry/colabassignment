#Q no.6 heuristic  value tic-tac-toe
class TicTacToeHeuristic:
    def __init__(self, board, player, opponent):
        """
        Initialize the Tic-Tac-Toe board and players.
        :param board: 3x3 list representing the current state of the board.
        :param player: Character representing the player (e.g., 'X').
        :param opponent: Character representing the opponent (e.g., 'O').
        """
        self.board = board
        self.player = player
        self.opponent = opponent

    def is_open(self, line):
        """
        Check if a line (row, column, or diagonal) is open for either player.
        A line is open if it contains only empty cells or one player's symbol.
        :param line: List of cells in the line.
        :return: (open_for_player, open_for_opponent) - tuple of booleans.
        """
        player_open = all(cell in [self.player, ' '] for cell in line)
        opponent_open = all(cell in [self.opponent, ' '] for cell in line)
        return player_open, opponent_open

    def count_open_lines(self):
        """
        Count the number of open lines for both the player and the opponent.
        :return: (open_for_player, open_for_opponent) - counts of open lines.
        """
        player_count = 0
        opponent_count = 0

        # Check rows and columns
        for i in range(3):
            row = self.board[i]
            col = [self.board[j][i] for j in range(3)]
            player_open_row, opponent_open_row = self.is_open(row)
            player_open_col, opponent_open_col = self.is_open(col)
            if player_open_row:
                player_count += 1
            if opponent_open_row:
                opponent_count += 1
            if player_open_col:
                player_count += 1
            if opponent_open_col:
                opponent_count += 1

        # Check diagonals
        main_diag = [self.board[i][i] for i in range(3)]
        anti_diag = [self.board[i][2 - i] for i in range(3)]
        player_open_main_diag, opponent_open_main_diag = self.is_open(main_diag)
        player_open_anti_diag, opponent_open_anti_diag = self.is_open(anti_diag)
        if player_open_main_diag:
            player_count += 1
        if opponent_open_main_diag:
            opponent_count += 1
        if player_open_anti_diag:
            player_count += 1
        if opponent_open_anti_diag:
            opponent_count += 1

        return player_count, opponent_count

    def calculate_heuristic(self):
        """
        Calculate the heuristic value e(p) for the current board state.
        :return: Heuristic value.
        """
        player_open, opponent_open = self.count_open_lines()
        return player_open - opponent_open


# Example usage
if __name__ == "__main__":
    # Define the current board state
    board = [
        ['X', ' ', ' '],
        [' ', 'X', ' '],
        [' ', ' ', ' ']
    ]
    player = 'X'
    opponent = 'O'

    # Create a TicTacToeHeuristic object
    ttt_heuristic = TicTacToeHeuristic(board, player, opponent)

    # Calculate and print the heuristic value
    heuristic_value = ttt_heuristic.calculate_heuristic()
    print("Heuristic value (e(p)):", heuristic_value)

