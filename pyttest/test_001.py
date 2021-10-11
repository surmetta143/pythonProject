import pytest
from selenium import webdriver
from pyttest.cutsomlogs import Test_Base_log


@pytest.fixture(scope="class")
def must_excute():
    print("i want this first")
@pytest.mark.usefixtures("must_excute")


class Test_all:
    log = Test_Base_log.log_name()
    def test_002(self):
        print("this is the scond test case")
        self.log.info("this test_002 logs information")

    def test_003(self):
        print("this is the third test case")
        self.log.info("this test_003 logs information")

    def test_004(self):
        print("this is the fourt test case")
        self.log.info("this is test_004 logs information")

    def test_001_1(self):
        print("this i s obtaed ftom test case 1")
        self.log.info("this test_001_1log information")

    def test_001_2(self):
        print("this is the second test case obtatef from test 1")
        self.log.info("this is test_001_2loginformation")
