# calculator_mod/commands/addition.py
"""A module for the Addition command."""
from calculator_mod.operations import Command

class Addition(Command):
    """Defines the Addition command"""

    def __init__(self, x, y):
        """Initialize the Addition command with operands x and y"""
        self.x = x
        self.y = y

    def execute(self):
        """Execute the Addition command and return the result"""
        return self.x + self.y
