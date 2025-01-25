#q no. 8 implement steepest ascent hill climbing for the 8 puzzle problem
import copy


class Puzzle:
    def __init__(self, initial_state, goal_state):
        self.state = initial_state
        self.goal = goal_state
        self.size = len(initial_state)  # Assuming a square grid (3x3)

    def find_blank(self, state):
        """Find the blank (zero) position in the puzzle."""
        for i in range(self.size):
            for j in range(self.size):
                if state[i][j] == 0:
                    return i, j

    def generate_neighbors(self, state):
        """Generate all possible neighbors by moving the blank tile."""
        neighbors = []
        blank_x, blank_y = self.find_blank(state)
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

        for move in moves:
            new_x, new_y = blank_x + move[0], blank_y + move[1]
            if 0 <= new_x < self.size and 0 <= new_y < self.size:
                new_state = copy.deepcopy(state)
                new_state[blank_x][blank_y], new_state[new_x][new_y] = (
                    new_state[new_x][new_y],
                    new_state[blank_x][blank_y],
                )
                neighbors.append(new_state)
        return neighbors

    def misplaced_tiles(self, state):
        """Heuristic: Count the number of misplaced tiles."""
        count = 0
        for i in range(self.size):
            for j in range(self.size):
                if state[i][j] != 0 and state[i][j] != self.goal[i][j]:
                    count += 1
        return count

    def manhattan_distance(self, state):
      """
      Heuristic: Calculate the Manhattan distance of tiles from their goal positions.
      """
      distance = 0
      for i in range(self.size):
        for j in range(self.size):
            if state[i][j] != 0:  # Ignore the blank tile
                # Find the goal position of the current tile
                goal_x, goal_y = [(x, y) for x in range(self.size) for y in range(self.size) if self.goal[x][y] == state[i][j]][0]
                # Calculate Manhattan distance
                distance += abs(goal_x - i) + abs(goal_y - j)
            return distance

    def steepest_ascent(self, heuristic="misplaced_tiles"):
        """Perform the Steepest Ascent Hill Climbing algorithm."""
        current_state = self.state
        current_heuristic = (
            self.misplaced_tiles(current_state)
            if heuristic == "misplaced_tiles"
            else self.manhattan_distance(current_state)
        )

        while True:
            neighbors = self.generate_neighbors(current_state)
            best_neighbor = None
            best_heuristic = float("inf")

            for neighbor in neighbors:
                neighbor_heuristic = (
                    self.misplaced_tiles(neighbor)
                    if heuristic == "misplaced_tiles"
                    else self.manhattan_distance(neighbor)
                )

                if neighbor_heuristic < best_heuristic:
                    best_heuristic = neighbor_heuristic
                    best_neighbor = neighbor

            if best_heuristic >= current_heuristic:
                # Local maximum reached
                break

            current_state = best_neighbor
            current_heuristic = best_heuristic

        return current_state, current_heuristic


if __name__ == "__main__":
    # Define initial and goal states
    initial_state = [
        [1, 2, 3],
        [4, 0, 6],
        [7, 5, 8],
    ]
    goal_state = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0],
    ]

    puzzle = Puzzle(initial_state, goal_state)

    # Solve using Steepest Ascent Hill Climbing with Misplaced Tiles heuristic
    final_state, heuristic_value = puzzle.steepest_ascent(heuristic="misplaced_tiles")

    print("Final State (Misplaced Tiles Heuristic):")
    for row in final_state:
        print(row)
    print("Heuristic Value:", heuristic_value)

    # Solve using Steepest Ascent Hill Climbing with Manhattan Distance heuristic
    final_state, heuristic_value = puzzle.steepest_ascent(heuristic="manhattan_distance")

    print("\nFinal State (Manhattan Distance Heuristic):")
    for row in final_state:
        print(row)
    print("Heuristic Value:", heuristic_value)

