#Q no.5 heuristic value of the states for Block world Problem
def calculate_heuristic(start_state, goal_state):
    """
    Calculate the heuristic value e(p) for the Blocks World problem.
    :param start_state: List of lists representing the current state.
    :param goal_state: List of lists representing the goal state.
    :return: Heuristic value e(p).
    """
    # Create a mapping of block -> correct support structure in goal state
    goal_support = {}
    for stack in goal_state:
        for i in range(len(stack)):
            block = stack[i]
            goal_support[block] = stack[:i]  # Support structure is all blocks below the current one

    # Initialize the heuristic value
    heuristic_value = 0

    # Check the support structure for each block in the start state
    for stack in start_state:
        for i in range(len(stack)):
            block = stack[i]
            current_support = stack[:i]  # Support structure is all blocks below the current one

            if current_support == goal_support.get(block, []):  # Correct support structure
                heuristic_value += len(current_support) + 1  # +1 for each block in the structure
            else:  # Incorrect support structure
                heuristic_value -= len(current_support) + 1  # -1 for each block in the structure

    return heuristic_value


# Example usage
if __name__ == "__main__":
    # Define the start state and goal state
    start_state = [["A", "D", "C", "B"]]  # All blocks in one stack
    goal_state = [["D"], ["C"], ["B"], ["A"]]  # Correct arrangement as per the image

    # Calculate heuristic value
    heuristic = calculate_heuristic(start_state, goal_state)
    print("Heuristic value (e(p)):", heuristic)
