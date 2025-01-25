#Q no.3 Implement DFS/BFS on the water jug problem to store in list.
from collections import deque

class WaterJug:
    def __init__(self, initial_state, goal_state):
        """
        Initialize the water jug problem with initial and goal states.
        :param initial_state: Tuple representing the initial state (jug1, jug2).
        :param goal_state: Tuple representing the goal state (jug1, jug2).
        """
        self.initial_state = initial_state
        self.goal_state = goal_state

    def goal_test(self, current_state):
        """
        Check if the current state is the goal state.
        :param current_state: Tuple representing the current state (jug1, jug2).
        :return: True if current_state matches goal_state, otherwise False.
        """
        return current_state == self.goal_state

    def successors(self, state):
        """
        Generate possible successor states based on the production rules.
        :param state: Tuple representing the current state (jug1, jug2).
        :return: List of successor states.
        """
        jug1, jug2 = state
        capacity1, capacity2 = 4, 3
        successors = set()

        # Rule 1: Fill jug1
        successors.add((capacity1, jug2))
        # Rule 2: Fill jug2
        successors.add((jug1, capacity2))
        # Rule 3: Empty jug1
        successors.add((0, jug2))
        # Rule 4: Empty jug2
        successors.add((jug1, 0))
        # Rule 5: Pour water from jug1 to jug2
        transfer = min(jug1, capacity2 - jug2)
        successors.add((jug1 - transfer, jug2 + transfer))
        # Rule 6: Pour water from jug2 to jug1
        transfer = min(jug2, capacity1 - jug1)
        successors.add((jug1 + transfer, jug2 - transfer))

        return [s for s in successors if s != state]

    def search(self, method="BFS"):
        """
        Perform DFS or BFS to find the solution.
        :param method: "BFS" or "DFS".
        :return: Path to the solution or None if no solution exists.
        """
        open_list = deque([self.initial_state])  # Use deque for BFS/DFS
        closed_list = {}  # Store state and parent
        closed_list[self.initial_state] = None

        while open_list:
            if method == "BFS":
                current_state = open_list.popleft()
            elif method == "DFS":
                current_state = open_list.pop()

            # Check if the goal state is reached
            if self.goal_test(current_state):
                return self.generate_path(closed_list, current_state)

            # Generate successors and process them
            for successor in self.successors(current_state):
                if successor not in closed_list:
                    closed_list[successor] = current_state
                    open_list.append(successor)

        return None  # No solution found

    def generate_path(self, closed_list, goal_state):
        """
        Generate the path from the initial state to the goal state.
        :param closed_list: Dictionary with state and parent mapping.
        :param goal_state: Tuple representing the goal state (jug1, jug2).
        :return: List of states from initial to goal state.
        """
        path = []
        state = goal_state
        while state is not None:
            path.append(state)
            state = closed_list[state]
        return path[::-1]

# Example
if __name__ == "__main__":
    initial_state = (4, 0)
    goal_state = (2, 0)

    water_jug = WaterJug(initial_state, goal_state)

    print("Using BFS:")
    path_bfs = water_jug.search(method="BFS")
    if path_bfs:
        print("Path to solution:", path_bfs)
    else:
        print("No solution found.")

    print("\nUsing DFS:")
    path_dfs = water_jug.search(method="DFS")
    if path_dfs:
        print("Path to solution:", path_dfs)
    else:
        print("No solution found.")
