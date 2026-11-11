"""31. Calculate Ace, face, red, and black card probabilities."""


def card_probabilities(cards):
    n = len(cards)
    ace = sum(c[:-1] == "A" for c in cards)
    face = sum(c[:-1] in {"J", "Q", "K"} for c in cards)
    red = sum(c[-1] in "HD" for c in cards)
    black = n - red
    counts = {"Ace": ace, "Face": face, "Red": red}
    return {k: v / n for k, v in counts.items()}, max(counts, key=counts.get), black / n


print(card_probabilities(["AH", "10D", "KC", "QS"]))
