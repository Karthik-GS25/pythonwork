"""37. Return matrix values in clockwise spiral order."""


def spiral_order(matrix):
    matrix = [row[:] for row in matrix]
    out = []
    while matrix:
        out += matrix.pop(0)
        if matrix and matrix[0]:
            for row in matrix:
                out.append(row.pop())
        if matrix:
            out += matrix.pop()[::-1]
        for row in matrix[::-1]:
            if row:
                out.append(row.pop(0))
    return out


print(spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
