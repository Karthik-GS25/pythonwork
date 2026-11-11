"""55. User-defined iterator producing decimal values."""


class NumberIterator:
    def __init__(self, start=0.0, stop=1.0, step=0.25):
        self.current = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.stop:
            raise StopIteration
        value = self.current
        self.current += self.step
        return value


print(list(NumberIterator()))
