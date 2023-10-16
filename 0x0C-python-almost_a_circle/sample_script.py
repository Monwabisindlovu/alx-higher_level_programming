#!/usr/bin/python3
"""
This is a sample Python script that demonstrates PEP 8 compliance and documentation.

It contains a function and a class with docstrings.

Author: Your Name
"""

# Global variable with a docstring
global_variable = 42
"""This is a global variable."""

def sample_function(param1, param2):
    """
    This function takes two parameters and returns their sum.

    Args:
        param1 (int): The first parameter.
        param2 (int): The second parameter.

    Returns:
        int: The sum of param1 and param2.
    """
    return param1 + param2

class SampleClass:
    """
    This is a sample class.

    Attributes:
        attr1 (str): A class attribute.
    """

    attr1 = "I'm a class attribute."

    def __init__(self, name):
        """
        Constructor for SampleClass.

        Args:
            name (str): The name of the instance.
        """
        self.name = name

    def greet(self):
        """
        A method to greet the instance.

        Returns:
            str: A greeting message.
        """
        return f"Hello, I'm {self.name}!"

if __name__ == "__main__":
    """ Sample usage of the script """
    result = sample_function(10, 20)
    print(f"Result of sample_function: {result}")

    obj = SampleClass("Alice")
    greeting = obj.greet()
    print(greeting)

