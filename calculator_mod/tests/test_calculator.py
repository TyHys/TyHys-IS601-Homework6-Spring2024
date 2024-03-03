"""Test the Calculator class in the calculator_mod module."""
from calculator_mod.calculator import Calculator
from calculator_mod.commands import Addition

def test_calculator_execute_command():
    """Test the execute_command method of the Calculator class."""
    calculator = Calculator()
    command = Addition(5, 3)
    result = calculator.execute_command(command)
    assert result == 8

def test_calculator_get_history():
    """Test the get_history method of the Calculator class."""
    calculator = Calculator()
    command = Addition(5, 3)
    calculator.execute_command(command)
    history = calculator.get_history()
    assert len(history) == 1
    assert history[0].execute() == 8
