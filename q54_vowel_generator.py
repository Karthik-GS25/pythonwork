"""54. Generator yielding vowels one at a time."""


def getvowels(name):
    for character in name:
        if character in "aeiouAEIOU":
            yield character


print(list(getvowels("Amrita")))
