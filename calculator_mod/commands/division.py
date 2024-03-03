# calculator_mod/commands/division.py
"""A module for the Division command."""
from calculator_mod.operations import Command

class Division(Command):
    """Defines the Division command"""

    def __init__(self, x, y):
        """Initialize the Division command with operands x and y"""
        self.x = x
        self.y = y

    def execute(self):
        """Execute the Division command and return the result"""
        if self.y == 0:
            raise ValueError("Cannot divide by zero!")
        return self.x / self.y
