"""62. Find a four-direction rat-maze path by backtracking."""


def rat_path(maze):
    n = len(maze)
    solution = [[0] * n for _ in range(n)]

    def go(r, c):
        if not (0 <= r < n and 0 <= c < n) or not maze[r][c] or solution[r][c]:
            return False
        solution[r][c] = 1
        if (r, c) == (n - 1, n - 1):
            return True
        if any(go(r + dr, c + dc) for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1))):
            return True
        solution[r][c] = 0
        return False

    return solution if go(0, 0) else None


print(rat_path([[1, 0, 0, 0], [1, 1, 0, 1], [0, 1, 0, 0], [1, 1, 1, 1]]))
