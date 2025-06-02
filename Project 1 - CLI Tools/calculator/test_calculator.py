# calculator/test_calculator.py

import pytest
import os
from operations import add, subtract, multiply, divide
from history import load_history, add_to_history, clear_history, HISTORY_FILE


def test_add():
    assert add(10, 5) == 15


def test_subtract():
    assert subtract(10, 5) == 5


def test_multiply():
    assert multiply(10, 5) == 50


def test_divide():
    assert divide(10, 5) == 2


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)


def test_history_operations():
    clear_history()
    add_to_history("add", 10, 5, 15)
    history = load_history()
    assert len(history) == 1
    assert history[0]["result"] == 15


def test_clear_history():
    clear_history()
    assert len(load_history()) == 0


def teardown_module(module):
    if os.path.exists(HISTORY_FILE):
        os.remove(HISTORY_FILE)