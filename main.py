"""
This is the main entry point of the Sudoku application.

The main function performs the following steps:
1. Loads the configuration.
2. Creates an instance of the Sudoku class.
3. Sets up the parameters, such as the target file, fixed cells, and custom cells.
4. Loads the Sudoku board from the target file.
5. Clears the board, setting all cell values to 0.
6. Customizes the board by setting values to the specified custom cells, if allowed.
7. Stores the customized board in a new file.
8. Prints a success message.

"""

from config import load_config
from sudoku import Sudoku

# Load the configuration
load_config()

def main():
    """
    The main function of the Sudoku application.

    """
    # Create an instance of the Sudoku class
    sudoku = Sudoku()

    # Set up parameters
    target = 'sudoku_board.txt'
    contains_fixed_cells = False

    if contains_fixed_cells:
        fixed_cells = [(0, 0, 0)]
    else:
        fixed_cells = []

    custom_cells = [
        (1, 1, 15),
        (2, 3, 4),
        (5, 6, 7),
        (0, 0, 0),
    ]

    # Load the Sudoku board from the target file
    board = sudoku.load_board(target)

    # Clear the board, setting all cell values to 0
    board = sudoku.clear_board(board)

    # Customize the board by setting values to the specified custom cells, if allowed
    board = sudoku.customize_board(board, contains_fixed_cells, fixed_cells, custom_cells)

    # Store the customized board in a new file
    message = sudoku.store_board(board, new_target='edited_sudoku_board.txt')

    # Print a success message
    print(message)


if __name__ == '__main__':
    main()
