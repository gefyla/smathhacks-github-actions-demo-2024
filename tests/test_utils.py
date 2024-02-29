"""
Let's pretend this is very robust test suite and we probably shouldn't alter tests.

(these tests are making sure that our very important library doesn't break our clients' code)
"""
import pytest
from src.utils import addition, subtraction, equivalence

def test_addition():
    a = 10
    b = 5
    assert addition(a, b) == 15

def test_subtraction():
    a = 10
    b = 5
    assert subtraction(a, b) == 5

def test_equivalence():
    a = 10
    b = 5
    assert not equivalence(a, b)
