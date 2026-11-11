"""63. Coin-toss game written for easy breakpoint/variable inspection."""

import random


def play(guess):
    toss = random.choice(("heads", "tails"))
    result = toss == guess.lower()
    return toss, result


guess = "heads"
toss, result = play(guess)
print(f"Toss: {toss}; guess correct: {result}")
