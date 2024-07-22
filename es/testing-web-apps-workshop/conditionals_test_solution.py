# Description: Tests for conditionals.py

import src.conditionals as conditionals


def test_greater_num():
    assert conditionals.greater_num(4, 5) == 5

def test_greater_num_2():
    assert conditionals.greater_num(5, 4) == 5

def test_greater_num_3():
    assert conditionals.greater_num(5, 5) == 5

def test_hello_world():
    assert conditionals.hello_world("es") == "Hola, Mundo"

def test_hello_world_2():
    assert conditionals.hello_world("pt") == "Olá, Mundo"

def test_hello_world_3():
    assert conditionals.hello_world("en") == "Hello, World"

