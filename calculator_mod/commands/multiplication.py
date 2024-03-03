# calculator_mod/commands/multiplication.py
"""A module for the Multiplication command."""
from calculator_mod.operations import Command

class Multiplication(Command):
    """Defines the Multiplication command"""

    def __init__(self, x, y):
        """Initialize the Multiplication command with operands x and y"""
        self.x = x
        self.y = y

    def execute(self):
        """Execute the Multiplication command and return the result"""
        return self.x * self.y
