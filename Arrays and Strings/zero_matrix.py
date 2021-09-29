# Given matrix, if an element in this N x N matrix is zero, set entire row and column to zero.
# O(N x N) time complexity, O(1) space complexity.

import numpy as np

def zero_entire_row(matrix, index):
    """Zeros out entire row."""

    for i in range(len(matrix)):
        matrix[index, i] = 0

    return matrix

def zero_entire_col(matrix, index):
    """Zeros out entire row."""

    for i in range(len(matrix)):
        matrix[i, index] = 0

    return matrix

def zero_rows_columns_matrix(matrix):
    """If an element in the matrix has a zero, also zero out the corresponding row and columns.
    
    Input, output: numpy matrix
    """

    length = len(matrix)

    first_row_zero = False
    first_col_zero = False

    # Check if first row or col needs to be zeroed
    for i in range(length):
        if matrix[i, 0] == 0:
            first_col_zero = True
        if matrix[0, i] == 0:
            first_row_zero = True

    # Store 0 in first row/column if the corresponding row/col has a zero
    for i in range(1, length):
        for j in range(1, length):
            if matrix[i, j] == 0:
                matrix[i, 0] = 0
                matrix[0, j] = 0
    
    # Zero corresponding rows/cols
    for i in range(1, length):
        if matrix[i, 0] == 0:
            zero_entire_row(matrix, i)
        if matrix[0, i] == 0:
            zero_entire_col(matrix, i)

    # Deal with the zeros being in the first index
    if matrix[0, 0] == 0:
        zero_entire_row(matrix, 0)
        zero_entire_col(matrix, 0)

    # Deal with first row or col being zero
    if first_col_zero:
        zero_entire_col(matrix, 0)
    if first_row_zero:
        zero_entire_row(matrix, 0)

    return matrix


if __name__ == "__main__":
    print(zero_rows_columns_matrix(np.matrix([[2, 3 , 4], [2, 1, 2], [1, 1, 1]])))
    print(zero_rows_columns_matrix(np.matrix([[2, 0 , 4], [2, 1, 2], [1, 1, 1]])))
    print(zero_rows_columns_matrix(np.matrix([[0, 0 , 4], [2, 1, 2], [1, 1, 1]])))
    print(zero_rows_columns_matrix(np.matrix([[2, 2 , 4], [2, 2, 2], [1, 1, 0]])))
    print(zero_rows_columns_matrix(np.matrix([[2, 2 , 4], [2, 0, 2], [1, 1, 0]])))
    print(zero_rows_columns_matrix(np.matrix([[0, 2 , 4], [2, 2, 2], [1, 1, 0]])))