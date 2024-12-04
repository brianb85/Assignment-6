"""
Iterable which produces an iterator of the Fibonacci series for a given value.
"""

class Fibonacci:

    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
        pass