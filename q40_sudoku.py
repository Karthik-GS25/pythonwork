"""40. Validate and solve a 9x9 Sudoku board."""


def solve_sudoku(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] not in ".123456789":
                return False, "Invalid character"

    def valid(r, c, ch):
        return (
            all(board[r][j] != ch for j in range(9))
            and all(board[i][c] != ch for i in range(9))
            and all(
                board[i][j] != ch
                for i in range(r // 3 * 3, r // 3 * 3 + 3)
                for j in range(c // 3 * 3, c // 3 * 3 + 3)
            )
        )

    def solve():
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    for ch in "123456789":
                        if valid(r, c, ch):
                            board[r][c] = ch
                            if solve():
                                return True
                            board[r][c] = "."
                    return False
        return True

    for r in range(9):
        for c in range(9):
            ch = board[r][c]
            if ch != ".":
                board[r][c] = "."
                ok = valid(r, c, ch)
                board[r][c] = ch
            else:
                ok = True
            if not ok:
                return False, "Duplicate value"
    return (True, board) if solve() else (False, "No solution")


print(
    solve_sudoku(
        [
            list("53..7...."),
            list("6..195...."),
            list(".98....6."),
            list("8...6...3"),
            list("4..8.3..1"),
            list("7...2...6"),
            list(".6....28."),
            list("...419..5"),
            list("....8..79"),
        ]
    )[0]
)
