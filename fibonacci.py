"""
Iterable which produces an iterator of the Fibonacci series for a given value.
"""


class Fibonacci:

    def __init__(self, value):
        int(value)
        self.value = value
        self.end = 0


    def __iter__(self):
        return self

    def __next__(self):
        if self.end > self.value:
            raise StopIteration

        self.end = 1
        return self.value

