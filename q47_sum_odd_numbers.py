"""47. Sum odd numbers three ways."""


def sum_odds_function(values):
    return sum(x for x in values if x % 2)


def sum_odds_comprehension(values):
    return sum([x for x in values if x % 2])


def is_odd(x):
    return x % 2 != 0


def sum_odds_user_function(values):
    return sum(filter(is_odd, values))


print(sum_odds_function([1, 2, 3, 4, 5]))
