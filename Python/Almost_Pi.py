__author__ = 'stevenschmatz'

import math

# TEST CASES
test_n = 200
test_abcd_list = [6, 75, 89, 226]

def f(n, k):
    return math.e ** (k / float(n)) - 1


def f_sum(n, abcd_list):
    return sum([f(n, x) for x in abcd_list])


def error(n, abcd_list):
    return f_sum(n, abcd_list) - math.pi