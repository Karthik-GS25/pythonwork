"""20. Decide word break and list every valid segmentation."""


def word_break(s, word_dict):
    words = set(word_dict)
    memo = {}

    def build(i):
        if i == len(s):
            return [""]
        if i in memo:
            return memo[i]
        out = []
        for j in range(i + 1, len(s) + 1):
            if s[i:j] in words:
                for tail in build(j):
                    out.append((s[i:j] + " " + tail).strip())
        memo[i] = out
        return out

    patterns = build(0)
    return bool(patterns), patterns


print(word_break("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
