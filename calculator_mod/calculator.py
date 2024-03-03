# calculator_mod/calculator.py

"""A module that defines the Calculator class"""

from calculator_mod.calculations import CalculationHistory
import logging

class Calculator:
    """Defines a Calculator class"""

    def __init__(self):
        self.history = CalculationHistory()

    def execute_command(self, command):
        """Executes a command and updates history"""
        result = command.execute()
        self.history.add_to_history(command)
        return result

    def get_history(self):
        """Retrieves the calculation history"""
        return self.history.get_history()

    def log_program_start(self):
        """Logs the start of the calculator program"""
        logging.info("Calculator program started.")

    def log_program_stop(self):
        """Logs the stop of the calculator program"""
        logging.info("Calculator program stopped.")
