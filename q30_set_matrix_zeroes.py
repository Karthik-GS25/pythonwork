"""30. Set matrix rows and columns containing zero to zero in place."""


def set_zeroes(matrix):
    rows = {i for i, row in enumerate(matrix) if 0 in row}
    cols = {
        j
        for j in range(len(matrix[0]))
        if any(matrix[i][j] == 0 for i in range(len(matrix)))
    }
    for i, row in enumerate(matrix):
        for j in range(len(row)):
            if i in rows or j in cols:
                row[j] = 0
    return matrix


print(set_zeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
