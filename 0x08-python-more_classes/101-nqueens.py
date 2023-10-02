#!/usr/bin/python3
import sys

def solveNQueens(n):
    """
    Solve the N-Queens problem and return all possible solutions.

    Args:
        n (int): The size of the chessboard and the number of queens.

    Returns:
        list: A list of solutions, where each solution is represented as a list of lists.
              Each inner list contains the row and column positions of queens.

    """
    def can_place(pos, ocuppied_positions):
        """
        Check if a queen can be placed at a given position without attacking others.

        Args:
            pos (int): The column position to check.
            ocuppied_positions (list): A list of occupied positions in previous rows.

        Returns:
            bool: True if the queen can be placed at the position, False otherwise.
        """
        for i in range(len(ocuppied_positions)):
            if pos == ocuppied_positions[i] or \
                    pos + len(ocuppied_positions) - i == ocuppied_positions[i] or \
                    pos - len(ocuppied_positions) + i == ocuppied_positions[i]:
                return False
        return True

    def place_queen(n, index, ocuppied_positions, result):
        """
        Recursively place queens on the chessboard and find solutions.

        Args:
            n (int): The size of the chessboard.
            index (int): The current row to place a queen.
            ocuppied_positions (list): A list of occupied positions in previous rows.
            result (list): A list to store found solutions.

        """
        if index == n:
            result.append(ocuppied_positions[:])
            return
        for i in range(n):
            if can_place(i, ocuppied_positions):
                ocuppied_positions.append(i)
                place_queen(n, index + 1, ocuppied_positions, result)
                ocuppied_positions.pop()

    result = []
    place_queen(n, 0, [], result)
    return result

def main():
    """
    Main function to handle command-line arguments and print solutions.

    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solveNQueens(n)
    for solution in solutions:
        formatted_solution = [[i, pos] for i, pos in enumerate(solution)]
        print(formatted_solution)

if __name__ == "__main__":
    main()
