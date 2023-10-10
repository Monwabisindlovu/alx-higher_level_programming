#!/usr/bin/python3

class MyClass:
    """
    Defines a MyClass with name and number attributes.
    """

    
def __init__(self, name, number):
        """
        Initializes a MyClass instance with the provided name and number.
        Args:
            name (str): The name of the MyClass instance.
            number (int): The number associated with the MyClass instance.
        """
        self.name = name
        self.number = number

def to_json(self):
        """
        Retrieves a dictionary representation of a MyClass instance.
        Returns:
            dict: A dictionary containing the MyClass instance's attributes.
        """
        my_class_json = {
            'name': self.name,
            'number': self.number
        }
        return my_class_json
