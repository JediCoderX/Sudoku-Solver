board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

SIZE = 9


def print_board(grid):

    for i in range(SIZE):
        if i % 3 == 0:
            print("- - - - - - - - - -")
        for j in range(SIZE):
            print(str(grid[i][j]) + " ", end="")
            if j % 9 == 8:
                print()
            if j % 3 == 2 and j != 8:
                print('|', end="")


def is_full(grid):
    for i in range(SIZE):
        for j in range(SIZE):
            if grid[i][j] == 0:
                return False
    return True


def is_legal(grid, row, col, num):

    # Row check
    for j in range(SIZE):
        if grid[row][j] == num:
            return False

    # Column check
    for i in range(SIZE):
        if grid[i][col] == num:
            return False

    # Box check
    box_row = row // 3 * 3
    box_col = col // 3 * 3
    for i in range(3):
        for j in range(3):
            if grid[i + box_row][j + box_col] == num:
                return False

    return True


def is_sovled(grid, row, col):
    if is_full(grid):
        return True

    if col == SIZE:
        row += 1
        col = 0

    if grid[row][col] > 0:
        return is_sovled(grid, row, col + 1)

    for num in range(1, 10):
        if is_legal(grid, row, col, num):
            grid[row][col] = num
            if is_sovled(grid, row, col + 1):
                return True

        grid[row][col] = 0
    return False


if (is_sovled(board, 0, 0)):
    print_board(board)
else:
    print("There is no solution for this sudoku")
