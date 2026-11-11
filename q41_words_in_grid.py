"""41. Find words that can be formed by four-direction grid walks."""


def find_words(board, words):
    R, C = len(board), len(board[0])
    found = []

    def exists(word):
        def go(r, c, i, seen):
            if i == len(word):
                return True
            if (
                not (0 <= r < R and 0 <= c < C)
                or (r, c) in seen
                or board[r][c] != word[i]
            ):
                return False
            seen.add((r, c))
            ok = any(
                go(r + dr, c + dc, i + 1, seen)
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1))
            )
            seen.remove((r, c))
            return ok

        return any(go(r, c, 0, set()) for r in range(R) for c in range(C))

    for word in words:
        if exists(word):
            found.append(word)
    return found


print(
    find_words(
        [list("oath"), list("pea t".replace(" ", "")), list("eat"), list("rain")],
        ["oath", "pea"],
    )
)
