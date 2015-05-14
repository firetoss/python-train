# -*- coding: utf-8 -*-
import math


def is_odd(x):
    return x % 2 == 1

print filter(is_odd, [1, 2, 3, 4, 5, 6, 7])


def is_prime(x):
    if x <= 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

print filter(is_prime, range(1, 100))
