# Author: Tommy Armstrong
# Date: 5/9/2020
# Class: CS 362 - Software Engineering II
# Assignment: A2 - TDD Hands On

import re

def check_pwd(pwd):
    if len(pwd) < 8 or 20 < len(pwd):
        return False
    if re.search('[a-z]', pwd) is None:
        return False
    if re.search('[A-Z]', pwd) is None:
        return False
    if re.search('[0-9]', pwd) is None:
        return False
    if re.search('[~`!@#$%^&*()_+\-=]', pwd) is None:
        return False
    return True
