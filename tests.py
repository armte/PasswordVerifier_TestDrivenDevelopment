# Author: Tommy Armstrong
# Date: 5/9/2020
# Class: CS 362 - Software Engineering II
# Assignment: A2 - TDD Hands On

import unittest
import random
import string
from check_pwd import check_pwd

def create_pwd(length):
    return random.choices((string.ascii_leters + string.digits), length)


class TestPwdChecker(unittest.TestCase):

    def test1(self):
        pwd = ''
        expected = False
        self.assertEqual(check_pwd(pwd), expected)

    def test2(self):
        pwd = 'aB1#0000'
        expected = True
        self.assertEqual(check_pwd(pwd), expected)


if __name__ == '__main__':
    unittest.main()
