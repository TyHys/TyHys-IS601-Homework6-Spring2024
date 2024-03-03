# calculator_mod/calculations.py
"""A module for the history of calculator operations class."""
class CalculationHistory:
    """A class to represent the calculation history of a Calculator instance."""
    def __init__(self):
        """Initialize an instance of CalculationHistory with an empty history list."""
        self.history = []

    def add_to_history(self, command):
        """Add a command object to the history list.

        Args:
            command: The command object to be added to the history list.
        """
        self.history.append(command)

    def get_history(self):
        """Retrieve the calculation history list and return it.

        Returns:
            list: The list containing the calculation history.
        """
        return self.history
