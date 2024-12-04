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