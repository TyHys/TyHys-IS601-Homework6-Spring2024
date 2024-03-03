# calculator_mod/operations.py
"""Module for the command pattern"""
from abc import ABC, abstractmethod

class Command(ABC):
    """Abstract base class for command objects"""

    @abstractmethod
    def execute(self):
        """Execute the command"""
        pass
