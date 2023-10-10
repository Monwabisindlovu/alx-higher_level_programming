Copy code
#!/usr/bin/python3
"""
Script for adding command-line arguments to a JSON file.
"""
import sys
import os.path
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

""" Check if the add_item.json file exists and load its content if it does """
file_exists = os.path.isfile('add_item.json')
if file_exists:
    my_list = load_from_json_file('add_item.json')
else:
    my_list = []

""" Add command-line arguments to the list """
my_list.extend(sys.argv[1:])

""" Save the updated list to add_item.json """
save_to_json_file(my_list, 'add_item.json')
