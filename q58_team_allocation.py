"""58. Allocate a random course project team from department groups."""

from collections import defaultdict
from itertools import combinations
from functools import reduce
from datetime import date
import random, math

students = [
    ("Anita", "CSE", 85),
    ("Rahul", "CSE", 78),
    ("Priya", "CSE", 92),
    ("Kiran", "AI", 88),
    ("Dev", "Data Science", 80),
    ("Sara", "Cyber Security", 90),
]


def allocate(size, people=students):
    groups = defaultdict(list)
    for person in people:
        groups[person[1]].append(person)
    options = [
        (dept, team)
        for dept, members in groups.items()
        if len(members) >= size
        for team in combinations(members, size)
    ]
    if not options:
        return None
    dept, team = random.choice(options)
    total = reduce(lambda a, p: a + p[2], team, 0)
    return {
        "team_size": size,
        "date": date.today(),
        "department": dept,
        "team": team,
        "total": total,
        "average": total / size,
    }


print(allocate(3))
