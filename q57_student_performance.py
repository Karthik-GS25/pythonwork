"""57. Student performance analyzer using standard-library modules."""

from collections import Counter
from functools import reduce
from datetime import date
import random

students = {
    "Tarun": [82, 91, 78],
    "Karthik": [65, 72, 68],
    "Chadrika": [91, 95, 89],
    "Trisha": [76, 81, 79],
    "Atul": [88, 84, 92],
}


def analyze(data=students):
    averages = {name: sum(marks) / len(marks) for name, marks in data.items()}
    highest = max(averages, key=averages.get)
    selected = random.choice(list(data))
    grades = Counter(
        "A" if average >= 90 else "B" if average >= 75 else "C"
        for average in averages.values()
    )
    total = reduce(
        lambda a, b: a + b, (mark for marks in data.values() for mark in marks), 0
    )
    return averages, highest, selected, date.today(), grades, total


print(analyze())
