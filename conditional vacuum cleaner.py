#Q no.2 Improve the vacuum cleaning agent’s efficiency by implementing a model-based agent
#A model-based vacuum cleaning agent maintains an internal representation of the environment, enabling it to make smarter decisions and avoid unnecessary actions.
#This approach is more efficient because the agent doesn't repeatedly visit clean areas or perform redundant cleaning.
#Instead, it remembers which areas are clean and focuses on dirty areas.
#Memory of the Environment:Tracks the state of all rooms.Avoids revisiting clean rooms unnecessarily.
#Planned Movement:Navigates intelligently based on known information.Reduces wasted moves and energy consumption.
#Adaptability:Adapts to dynamic changes in the environment (e.g., a room becoming dirty again).
class ModelBasedVacuumCleaner:
    def __init__(self, environment):
        """
        Room situations:
                            {'A': 'dirty', 'B': 'clean', 'C': 'dirty'}
        """
        self.environment = environment  # Actual environment
        self.model = environment.copy()  # Internal model of the environment
        self.current_location = 'A'  # Starting location

    def sense_environment(self):
        """
        The current state of the environment.
        """
        return self.environment[self.current_location]

    def update_model(self, location, state):
        """
        Update the internal model of the environment.
        :param location: Location to update.
        :param state: New state of the location.
        """
        self.model[location] = state

    def clean(self):
        """
        Clean the current location.
        """
        print(f"Cleaning {self.current_location}...")
        self.environment[self.current_location] = 'clean'
        self.update_model(self.current_location, 'clean')

    def move(self):
        """
        Move to the next location based on the internal model.
        """
        # Find the next dirty location
        for location, state in self.model.items():
            if state == 'dirty':
                self.current_location = location
                print(f"Moved to {self.current_location}.")
                return
        print("All locations are clean. Stopping.")

    def reflex_agent_with_model(self):
        """
        Model-based reflex agent logic:
        - If the current location is dirty, clean it and update the model.
        - Otherwise, move to the next dirty location based on the model.
        """
        if self.sense_environment() == 'dirty':
            self.clean()
        else:
            self.move()

    def run(self):
        """
        Run the vacuum cleaner until all rooms are clean.
        """
        steps = 0
        while 'dirty' in self.model.values():
            print(f"Step {steps + 1}:")
            self.reflex_agent_with_model()
            print(f"Model state: {self.model}")
            print(f"Environment state: {self.environment}")
            print("-" * 20)
            steps += 1
        print("All rooms are clean.")

# Example usage:
if __name__ == "__main__":
    # Initial environment state
    environment = {'A': 'dirty', 'B': 'dirty', 'C': 'clean'}

    # Create the vacuum cleaner
    vacuum = ModelBasedVacuumCleaner(environment)

    # Run the vacuum cleaner
    vacuum.run()
