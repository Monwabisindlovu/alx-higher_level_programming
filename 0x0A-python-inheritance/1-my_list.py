#!/usr/bin/python3
class MyList(list):
    def print_sorted(self):
        """Print the list, but sorted in ascending order."""
        print(sorted(self))
