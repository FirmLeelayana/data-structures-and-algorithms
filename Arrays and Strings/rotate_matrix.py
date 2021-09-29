# Rotate matrix of integers by 90 degrees.
# Time complexity: O(n^2), space complexity: O(1)

import numpy as np
import math

def rotate_matrix_ninety_degrees(matrix):
    """Rotates a numpy matrix by ninety degrees.
    
    Input: matrix, numpy matrix
    Output: rotated_matrix, numpy matrix
    """

    length = len(matrix)
    number_of_layers = math.ceil(length / 2)

    if length % 2 == 1:
        number_of_layers -= 1 # Edge case: center value in matrix remains the same for odd lengths

    for i in range(number_of_layers):
        for j in range(length - 1):
            # Swapping ring by ring, index by index
            temp_index = matrix[i, j]
            matrix[i, j] = matrix[length - j - 1, i]
            matrix[length - j - 1, i] = matrix[length - i - 1, length - j - 1]
            matrix[length - i - 1, length - j - 1] = matrix[j, length - i - 1]
            matrix[j, length - i - 1] = temp_index

    return matrix


if __name__ == "__main__":
    print(rotate_matrix_ninety_degrees(np.matrix([[1, 2], [3, 4]])))
    print(rotate_matrix_ninety_degrees(np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])))

