"""8. Check whether max-merging safe triplets can form target."""


def merge_triplets(triplets, target):
    found = [False] * 3
    for triplet in triplets:
        if all(a <= b for a, b in zip(triplet, target)):
            for i, a in enumerate(triplet):
                if a == target[i]:
                    found[i] = True
    return all(found)


print(merge_triplets([[2, 5, 3], [1, 7, 5]], [2, 7, 5]))
