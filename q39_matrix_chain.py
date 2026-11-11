"""39. Matrix-chain minimum cost and parenthesization."""


def matrix_chain_order(dimensions):
    n = len(dimensions) - 1
    dp = [[0] * n for _ in range(n)]
    split = [[0] * n for _ in range(n)]
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float("inf")
            for k in range(i, j):
                cost = (
                    dp[i][k]
                    + dp[k + 1][j]
                    + dimensions[i] * dimensions[k + 1] * dimensions[j + 1]
                )
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    split[i][j] = k

    def text(i, j):
        if i == j:
            return f"A{i+1}"
        k = split[i][j]
        return "(" + text(i, k) + " x " + text(k + 1, j) + ")"

    return (0, "") if not n else (dp[0][n - 1], text(0, n - 1))


print(matrix_chain_order([10, 30, 5, 60]))
