#!/usr/bin/python3
import sys

args = sys.argv[1:]
num_args = len(args)

print(f"Number of argument{'s' if num_args != 1 else ''}: {num_args}{':' if num_args > 0 else '.'}")

for i, arg in enumerate(args, start=1):
    print(f"{i}: {arg}")

