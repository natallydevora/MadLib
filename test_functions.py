"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

from functions import *

##
##

def test_blank_1():
    test_1 = blank_1('')
    assert test_1 == 'Santa Clause is a ' + ' man '


def test_blank_2():
    test_2 = blank_2('')
    assert test_2 == 'who wears a ' + ' '
