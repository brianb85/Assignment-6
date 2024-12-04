"""
Test the Fibonacci module
"""

import pytest
from fibonacci import Fibonacci

def test_value_is_int():
    with pytest.raises(ValueError):
        Fibonacci("asd")

def test_value_0():
    assert list(Fibonacci(0)) == [0]

def test_value_01():
    assert list(Fibonacci(1)) == [0, 1]

def test_value_011():
    assert list(Fibonacci(2)) == [0, 1, 1]

def test_value_01123():
    assert list(Fibonacci(4)) == [0, 1, 1, 2, 3]