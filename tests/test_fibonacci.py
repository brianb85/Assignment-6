"""
Test the Fibonacci module
"""

import pytest
from fibonacci import Fibonacci

def test_value_is_int():
    with pytest.raises(ValueError):
        Fibonacci("asd")