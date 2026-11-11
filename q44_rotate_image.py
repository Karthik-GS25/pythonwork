"""44. Rotate a square matrix clockwise in place."""


def rotate(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()
    return matrix


print(rotate([[1, 2], [3, 4]]))
