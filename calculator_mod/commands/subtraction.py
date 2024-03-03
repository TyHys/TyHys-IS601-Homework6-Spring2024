# calculator_mod/commands/subtraction.py
"""A module for the Subtraction command."""
from calculator_mod.operations import Command

class Subtraction(Command):
    """Defines the Subtraction command"""

    def __init__(self, x, y):
        """Initialize the Subtraction command with operands x and y"""
        self.x = x
        self.y = y

    def execute(self):
        """Execute the Subtraction command and return the result"""
        return self.x - self.y
