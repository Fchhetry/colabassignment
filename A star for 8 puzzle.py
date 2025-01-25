#Q no.7 A* algorithm for 8 puzzle problems
import heapq

# Goal state
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# Directional moves for sliding tiles (up, down, left, right)
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

class PuzzleState:
    def __init__(self, state, blank_pos, g, parent=None):
        self.state = state
        self.blank_pos = blank_pos  # Position of the blank tile (0)
        self.g = g  # Cost from the start to this state (path cost)
        self.parent = parent  # Parent state (to reconstruct the solution path)
        self.h = self.manhattan_distance()  # Heuristic cost (Manhattan distance)
        self.f = self.g + self.h  # Total cost (g + h)

    def __lt__(self, other):
        return self.f < other.f

    def manhattan_distance(self):
        """Calculate the Manhattan Distance heuristic."""
        distance = 0
        for i in range(3):
            for j in range(3):
                val = self.state[i][j]
                if val != 0:  # Ignore the blank tile
                    target_x, target_y = divmod(val - 1, 3)
                    distance += abs(i - target_x) + abs(j - target_y)
        return distance

    def get_neighbors(self):
        """Generate neighboring states by sliding the blank tile."""
        neighbors = []
        x, y = self.blank_pos
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                # Swap blank with the neighboring tile
                new_state = [row[:] for row in self.state]
                new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
                neighbors.append(PuzzleState(new_state, (nx, ny), self.g + 1, self))
        return neighbors

    def is_goal(self):
        """Check if the current state is the goal state."""
        return self.state == goal_state

def a_star(start_state):
    """Solve the 8-puzzle using A* search algorithm."""
    # Initial state
    start_blank_pos = next((i, j) for i in range(3) for j in range(3) if start_state[i][j] == 0)
    start_puzzle_state = PuzzleState(start_state, start_blank_pos, 0)

    # Open list (priority queue)
    open_list = []
    heapq.heappush(open_list, start_puzzle_state)

    # Closed list (set of visited states)
    closed_list = set()

    while open_list:
        # Pop the state with the lowest f value
        current_state = heapq.heappop(open_list)

        # If it's the goal state, reconstruct and return the solution
        if current_state.is_goal():
            path = []
            while current_state:
                path.append(current_state.state)
                current_state = current_state.parent
            return path[::-1]  # Return reversed path

        closed_list.add(tuple(map(tuple, current_state.state)))

        # Generate neighbors and add them to the open list
        for neighbor in current_state.get_neighbors():
            if tuple(map(tuple, neighbor.state)) not in closed_list:
                heapq.heappush(open_list, neighbor)

    return None  # No solution found

def print_solution(solution):
    """Print the solution."""
    if solution:
        for step in solution:
            for row in step:
                print(row)
            print()
    else:
        print("No solution found.")

# Example usage
start_state = [
    [8, 1, 3],
    [4, 0, 2],
    [7, 6, 5]
]

solution = a_star(start_state)
print_solution(solution)