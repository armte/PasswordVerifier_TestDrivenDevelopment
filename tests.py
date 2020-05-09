# Author: Tommy Armstrong
# Date: 5/9/2020
# Class: CS 362 - Software Engineering II
# Assignment: A2 - TDD Hands On

import unittest
from random import choices, randint
import string
from check_pwd import check_pwd

def valid_pwd(length):
    assert(length >= 4)
    symbols = '~`!@#$%^&*()_+-='
    pwd = choices(string.ascii_lowercase, k=1)
    pwd += choices(string.ascii_uppercase, k=1)
    pwd += choices(string.digits, k=1)
    pwd += choices(symbols, k=1)
    prefix_len = len(pwd)
    pwd += choices((string.ascii_letters + string.digits + symbols), k=length-prefix_len)
    return ''.join(pwd)


class TestPwdChecker(unittest.TestCase):

    def test1(self):
        pwd = ''
        expected = False
        self.assertEqual(check_pwd(pwd), expected)

    def test2(self):
        pwd = 'aB1#0000'
        expected = True
        self.assertEqual(check_pwd(pwd), expected)

    def test3(self):
        pwd = 'aB1#0000000000000000'
        expected = True
        self.assertEqual(check_pwd(pwd), expected)

    def test4(self):
        pwd = 'aB1#0000000000'
        expected = True
        self.assertEqual(check_pwd(pwd), expected)

    def test5(self):
        pwd = 'B1#000000000'
        expected = False
        self.assertEqual(check_pwd(pwd), expected)

    def test6(self):
        pwd = 'a1#000000000'
        expected = False
        self.assertEqual(check_pwd(pwd), expected)

    def test7(self):
        pwd = 'aB#*********'
        expected = False
        self.assertEqual(check_pwd(pwd), expected)

    def test8(self):
        pwd = 'aB1000000000'
        expected = False
        self.assertEqual(check_pwd(pwd), expected)

    def test9(self):
        for i in range(5):
            length = randint(8, 20)
            pwd = valid_pwd(length)
            expected = True
            self.assertEqual(check_pwd(pwd), expected)

    def test10(self):
        for i in range(6):
            if i < 3:
                length = randint(4, 7)
            else:
                length = randint(21, 29)
            pwd = valid_pwd(length)
            expected = False
            self.assertEqual(check_pwd(pwd), expected)


if __name__ == '__main__':
    unittest.main()
