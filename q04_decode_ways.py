"""4. Count and list all decodings of digits 1-26."""


def decode_ways(s):
    if not s:
        return 0, []

    def build(index):
        if index == len(s):
            return [""]
        if s[index] == "0":
            return []
        result = []
        for size in (1, 2):
            part = s[index : index + size]
            if len(part) == size and 1 <= int(part) <= 26:
                for tail in build(index + size):
                    result.append(chr(64 + int(part)) + tail)
        return result

    patterns = build(0)
    return len(patterns), patterns


print(decode_ways("226"))
