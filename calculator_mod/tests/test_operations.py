"""Tests for the operations module."""
from calculator_mod.operations import Command

class ConcreteCommand(Command):
    """A concrete command that inherits from the Command class."""
    def execute(self):
        return "executed"

def test_concrete_command_execute():
    """Test the execute method of the ConcreteCommand class."""
    command = ConcreteCommand()
    assert command.execute() == "executed"
