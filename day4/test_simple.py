"""
Testing of simple math operations
"""
from simple_math import *

def test_simple_add():
    assert simple_add(2,5) == 7

def test_simple_sub():
    assert simple_sub(1,7) == -6

def test_simple_mult():
    assert simple_mult(3,4) == 12

def test_simple_div():
    assert simple_div(63,7) == 9

def test_poly_first():
    assert poly_first(2, 3, 8) == 19

def test_poly_second():
    assert poly_second(5, 6, 2, 4) == 116

