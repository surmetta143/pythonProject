import pytest
from selenium import webdriver
@pytest.fixture()
def setup():
    print("this is the first")


def test_003(setup):
    print("this is the third test case")

def test_004(setup):
    print("this is the fourt test case")
def test_001_1():
    print("this i s obtaed ftom test case 1")
def test_001_2():
    print("this is the second test case obtatef from test 1")
def test_003_1():
    print("this is obtatted from test3")
