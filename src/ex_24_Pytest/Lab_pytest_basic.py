# pip pytest install

import pytest
@pytest.mark.smoke
def test_method1():
    print("Hello World")
    assert 5 == 6

@pytest.mark.smoke
def test_method2():
    print("Hello World")
    assert 5 == 5

import pytest
@pytest.mark.smoke
def test_method2():
    print("test1")
    assert 1-1 == 2

@pytest.mark.regression
def test_login():
    print("test2")
    assert 1 + 1 == 2