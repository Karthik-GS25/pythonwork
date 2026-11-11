"""49. Closure retaining values for a cumulative average."""


def cumulative_average():
    values = []

    def add(number):
        values.append(number)
        return sum(values) / len(values)

    return add


average = cumulative_average()
print(average(10), average(20))
