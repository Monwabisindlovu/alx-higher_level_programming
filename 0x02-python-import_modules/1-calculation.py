#!/usr/bin/python3
# Import functions from calculator_1.py
from calculator_1 import add, sub, mul, div

# Check if the script is being run as the main program
if __name__ == "__main__":
    # Define the values of a and b
    a = 10
    b = 5

    # Perform the operations and print the results
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))

