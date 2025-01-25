#Q.no1 Automated vacuum cleaner reflex agent

class VacuumCleaner:
    def __init__(self, environment):
        """
        room conditions{'A': 'dirty', 'B': 'clean'}
        """
        self.environment = environment
        self.current_location = 'A'  # Starting location of the vacuum cleaner

    def sense_environment(self):
        """
        Check the current location's state.
        """
        return self.environment[self.current_location]

    def clean(self):
        """
        Clean the current location.
        """
        print(f"Cleaning {self.current_location}...")
        self.environment[self.current_location] = 'clean'

    def move(self):
        """
        Move to the next location.
        """
        if self.current_location == 'A':
            self.current_location = 'B'
        else:
            self.current_location = 'A'
        print(f"Moved to {self.current_location}.")

    def reflex_agent(self):
        """
        Reflex agent logic:
        - If the current location is dirty, clean it.
        - Otherwise, move to the next location.
        """
        if self.sense_environment() == 'dirty':
            self.clean()
        else:
            self.move()

    def run(self, steps=10):
        """
        Run the vacuum cleaner for a specified number of steps.
        :param steps: Number of steps to run.
        """
        for step in range(steps):
            print(f"Step {step + 1}:")
            self.reflex_agent()
            print(f"Environment state: {self.environment}")
            print("-" * 20)


# Example usage:
if __name__ == "__main__":
    # Initial environment state
    environment = {'A': 'dirty', 'B': 'dirty'}

    # Create the vacuum cleaner
    vacuum = VacuumCleaner(environment)

    # Run the vacuum cleaner
    vacuum.run(steps=5)
