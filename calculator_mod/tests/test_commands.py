"""Test the commands module."""
from calculator_mod.commands import Subtraction, Multiplication, Division

def test_subtraction(random_number):
    """Test the Subtraction command."""
    for num in random_number:
        x = num
        y = num
        command = Subtraction(x, y)
        assert command.execute() == x - y

def test_multiplication(random_number):
    """Test the Multiplication command."""
    for num in random_number:
        x = num
        y = num
        command = Multiplication(x, y)
        assert command.execute() == x * y

def test_division(random_number):
    """Test the Division command."""
    for num in random_number:
        x = num + 1  # Ensure x is not zero
        y = num
        command = Division(x, y)
        assert command.execute() == x / y
