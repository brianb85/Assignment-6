"""
Iterable which produces an iterator of the Fibonacci series for a given value.
"""


class Fibonacci:

    def __init__(self, value):
        int(value)
        self.value = value
        self.stop = 0

        self.start = 0
        self.next = 1


    def __iter__(self):
        return self

    def __next__(self):
        self.current_value = self.start
        if self.stop > self.value:
            raise StopIteration
        self.stop += 1
        self.start = self.next
        return self.current_value

