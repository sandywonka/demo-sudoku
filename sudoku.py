class Sudoku:
    """
    A class representing Sudoku board and operations.

    Methods:
        load_board(target)
        show_board(board)
        clear_board(board)
        customize_board(board, contains_fixed_cells, fixed_cells, custom_cells)
        store_board(board, new_target)
    """

    def load_board(self, target):
        """
        Load a Sudoku board from a file.

        Args:
            target (str): The path to the file containing the Sudoku board.

        Returns:
            list: A 2-dimensional list representing the Sudoku board.

        Raises:
            FileNotFoundError: If the specified file does not exist.
        """
        with open(target, 'r') as f:
            board = f.readlines()

        return self.show_board(board)

    def show_board(self, board):
        """
        Convert the board representation from string format to a 2-dimensional list.

        Args:
            board (list): A list of strings representing the Sudoku board.

        Returns:
            list: A 2-dimensional list representing the Sudoku board with integer values.

        Raises:
            ValueError: If the board format is invalid.
        """
        sudoku_board = []
        for line in board:
            row = [int(_) for _ in line.strip().split(',')]
            sudoku_board.append(row)

        return sudoku_board

    def clear_board(self, board):
        """
        Clear the Sudoku board by setting all cells to 0.

        Args:
            board (list): A 2-dimensional list representing the Sudoku board.

        Returns:
            list: The cleared Sudoku board.
        """
        return [[0] * len(row) for row in board]

    def customize_board(self, board, contains_fixed_cells, fixed_cells, custom_cells):
        """
        Customize the Sudoku board by updating specific cells with custom values.

        Args:
            board (list): A 2-dimensional list representing the Sudoku board.
            contains_fixed_cells (bool): Indicates whether the board contains fixed cells.
            fixed_cells (list): A list of tuples representing the coordinates and values of fixed cells.
            custom_cells (list): A list of tuples representing the coordinates and values to customize.

        Returns:
            list: The customized Sudoku board.

        Raises:
            ValueError: If an attempt is made to change a fixed cell.
        """
        for row, col, value in custom_cells:
            if (row, col, value) not in fixed_cells:
                board[row][col] = value
            else:
                raise ValueError(f"Cannot change the fixed cells: {fixed_cells}")

        return board

    def store_board(self, board, new_target):
        """
        Store the Sudoku board in a file.

        Args:
            board (list): A 2-dimensional list representing the Sudoku board.
            new_target (str): The path to the file to store the Sudoku board.

        Returns:
            str: A success message indicating the storage of the Sudoku board.

        Raises:
            PermissionError: If the file cannot be created or written to.
        """
        board_str = '\n'.join(','.join(str(cell) for cell in row) for row in board)

        with open(new_target, 'w') as f:
            f.write(board_str)

        return f"Successfully stored as {new_target}"
