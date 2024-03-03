# main.py

import importlib
import logging
from calculator_mod.calculator import Calculator

logging.basicConfig(filename='calculator_mod/logs/calculator.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_command(operator, operands):
    """Create the appropriate command object based on the operator."""
    try:
        # Convert the operator to the corresponding command class name
        command_class_name = operator_to_class_name(operator)

        # Dynamically import the command class
        module = importlib.import_module("calculator_mod.commands")
        command_class = getattr(module, command_class_name)

        # Create and return the command object
        return command_class(*operands)
    except (ImportError, AttributeError):
        print(f"Invalid operation: {operator}. Please enter a valid operator (+, -, *, /).")
        return None

def operator_to_class_name(operator):
    """Convert an operator to the corresponding command class name."""
    return {
        "+": "Addition",
        "-": "Subtraction",
        "*": "Multiplication",
        "/": "Division",
    }.get(operator)

def main():
    """Main function to demonstrate the usage of the Calculator class."""
    # Create an instance of the Calculator class
    calculator = Calculator()
    
    # Log program start
    logging.info("Calculator program started.")

    print("Welcome to the Calculator REPL!")
    print("Enter 'quit' to exit.")

    while True:
        # Prompt the user for input
        user_input = input(">>> ")

        # Check if the user wants to quit
        if user_input.lower() == "quit":
            print("Exiting Calculator.")
            # Log program stop
            logging.info("Calculator program stopped.")
            break

        # Split the input into operands and operator
        try:
            operands = user_input.split()
            operator = operands.pop(-2)
            operands = [float(operand) for operand in operands]
        except ValueError:
            print("Invalid input. Please enter a valid expression.")
            continue

        # Log user input
        logging.info(f"User input: {user_input}")

        # Create the appropriate command object based on the operator
        command = create_command(operator, operands)
        if command is None:
            continue

        # Execute the command
        try:
            result = calculator.execute_command(command)
            # Log output
            logging.info(f"Output: {result}")
        except ZeroDivisionError:
            print("Error: Division by zero.")
            continue

        # Print the result
        print("Result:", result)

if __name__ == "__main__":
    main()
