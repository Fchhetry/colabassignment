#Q no.3 implementing water jug problem with boolean goal and successor
from collections import deque

class WaterJug:
    def __init__(self, jug4_capacity, jug3_capacity, goal):
        self.jug4_capacity = jug4_capacity
        self.jug3_capacity = jug3_capacity
        self.goal = goal
        self.initial_state = (jug4_capacity, 0)  # (4L jug, 3L jug)

    def goalTest(self, current_state):
        """Check if the current state is the goal state."""
        return current_state[0] == self.goal

    def successor(self, current_state):
        """Generate all possible successor states."""
        x, y = current_state
        successors = []

        # Fill the 4L jug
        if x < self.jug4_capacity:
            successors.append((self.jug4_capacity, y))

        # Fill the 3L jug
        if y < self.jug3_capacity:
            successors.append((x, self.jug3_capacity))

        # Empty the 4L jug
        if x > 0:
            successors.append((0, y))

        # Empty the 3L jug
        if y > 0:
            successors.append((x, 0))

        # Pour water from 4L jug to 3L jug
        if x > 0 and y < self.jug3_capacity:
            pour = min(x, self.jug3_capacity - y)
            successors.append((x - pour, y + pour))

        # Pour water from 3L jug to 4L jug
        if y > 0 and x < self.jug4_capacity:
            pour = min(y, self.jug4_capacity - x)
            successors.append((x + pour, y - pour))

        return successors

    def DFS(self):
        """Depth First Search to find the solution."""
        initial_state = self.initial_state
        stack = [(initial_state, [])]  # stack stores (state, path)
        visited = set()  # to track visited states

        while stack:
            current_state, path = stack.pop()

            # Check if the state is the goal
            if self.goalTest(current_state):
                return path + [current_state]

            if current_state not in visited:
                visited.add(current_state)
                for neighbor in self.successor(current_state):
                    if neighbor not in visited:
                        stack.append((neighbor, path + [current_state]))

        return None  # No solution found

    def BFS(self):
        """Breadth First Search to find the solution."""
        initial_state = self.initial_state
        queue = deque([(initial_state, [])])  # queue stores (state, path)
        visited = set()  # to track visited states

        while queue:
            current_state, path = queue.popleft()

            # Check if the state is the goal
            if self.goalTest(current_state):
                return path + [current_state]

            if current_state not in visited:
                visited.add(current_state)
                for neighbor in self.successor(current_state):
                    if neighbor not in visited:
                        queue.append((neighbor, path + [current_state]))

        return None  # No solution found

    def generate_path(self, solution):
        """Generates the path from start to goal."""
        if solution:
            print("Solution path:")
            for state in solution:
                print(f"4L jug: {state[0]}L, 3L jug: {state[1]}L")
        else:
            print("No solution found.")

# Example usage:
goal = 2  # We want exactly 2 liters in the 4-liter jug
water_jug = WaterJug(4, 3, goal)

# DFS Solution
print("Depth First Search Solution:")
dfs_solution = water_jug.DFS()
water_jug.generate_path(dfs_solution)

# BFS Solution
print("\nBreadth First Search Solution:")
bfs_solution = water_jug.BFS()
water_jug.generate_path(bfs_solution)
