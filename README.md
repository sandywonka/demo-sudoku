# Sudoku

A Python class for representing Sudoku boards and performing various operations on them.

## Description

This Sudoku class provides methods to load, display, customize, clear, and store Sudoku boards. It supports reading Sudoku boards from files, converting board representations, clearing the board, customizing cells, and storing boards in files.

## Features

- Load a Sudoku board from a file
- Convert the board representation from string format to a 2-dimensional list
- Clear the Sudoku board by setting all cells to 0
- Customize the Sudoku board by updating specific cells with custom values
- Handle fixed cells and prevent changes to them
- Store the Sudoku board in a file

## Note
Don't forget to install the dependencies inside the requirements.txt
```bash
    pip install -r requirements.txt or pip3 install -r requirements.txt
```

## Usage
I've declared all of the method inside main.py files so you can simply call:
```python
    python main.py or python3 main.py
```
## Breaking Down

1. Instantiate the Sudoku class:

    ```python
    sudoku = Sudoku()
    ```

2. Load a Sudoku board from a file:

    ```python
    board = sudoku.load_board("path/to/board.txt")
    ```

3. Display the Sudoku board:

    ```python
    sudoku.show_board(board)
    ```

4. Clear the Sudoku board:

    ```python
    cleared_board = sudoku.clear_board(board)
    ```

5. Customize the Sudoku board:

    ```python
    contains_fixed_cells = True
    fixed_cells = [(0, 0, 5), (1, 1, 8)]  # (row, column, value)
    custom_cells = [(0, 2, 7), (1, 3, 2)]
    customized_board = sudoku.customize_board(board, contains_fixed_cells, fixed_cells, custom_cells)
    ```

6. Store the Sudoku board in a file:

    ```python
    sudoku.store_board(customized_board, "path/to/new_board.txt")
    ```

## Requirements

- Python 3.x

## License

This code is licensed under the [MIT License](LICENSE).

