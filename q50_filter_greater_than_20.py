"""50. Decorator and filter remove values greater than 20."""


def limit_to_20(function):
    def wrapper(values):
        return list(filter(lambda value: value <= 20, function(values)))

    return wrapper


@limit_to_20
def identity(values):
    return values


print(identity([5, 21, 20, 30]))
