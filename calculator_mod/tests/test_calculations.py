"""Test the CalculationHistory class in the calculations module."""
from calculator_mod.calculations import CalculationHistory

def test_add_to_history():
    """Test the add_to_history method of the CalculationHistory class."""
    history = CalculationHistory()
    assert len(history.get_history()) == 0

    history.add_to_history("command1")
    assert len(history.get_history()) == 1
    assert history.get_history() == ["command1"]

    history.add_to_history("command2")
    assert len(history.get_history()) == 2
    assert history.get_history() == ["command1", "command2"]

def test_get_history():
    """Test the get_history method of the CalculationHistory class."""
    history = CalculationHistory()
    assert not history.get_history()

    history.add_to_history("command1")
    assert history.get_history() == ["command1"]

    history.add_to_history("command2")
    assert history.get_history() == ["command1", "command2"]
