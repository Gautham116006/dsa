def traverse_matrix_clockwise(matrix):
    n = len(matrix)

    top_row = 0
    right_column = n - 1
    bottom_row = n - 1
    left_column = 0

    while top_row <= bottom_row and left_column <= right_column:

        # traverse top row
        for i in range(left_column, right_column + 1):
            matrix[top_row][i] = n - 1

        top_row += 1
        # end for

        # traverse right column
        for i in range(top_row, bottom_row + 1):
            matrix[i][right_column] = n - 1

        right_column -= 1
        # end for

        # traverse bottom row
        for i in range(right_column, left_column - 1, -1):
            matrix[bottom_row][i] = n - 1

        bottom_row -= 1
        # end for

        # traverse left row
        for i in range(bottom_row, top_row - 1, -1):
            matrix[i][left_column] = n - 1

        left_column += 1
        # end for

        n -= 1
    # end while

    for row in matrix:
        print(row)
    # end for


def create_matrix(size):
    m = []
    row = [0] * size
    for i in range(size):
        m.append(row)
    # end for


traverse_matrix_clockwise([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
