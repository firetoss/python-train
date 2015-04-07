# -*- coding: utf-8 -*-
def f(x):
    return x * x

print map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])

print map(str,  [1, 2, 3, 4, 5, 6, 7, 8, 9])


def add(x, y):
    return x + y

print reduce(add, [1, 3, 5, 7, 9])


def fn(x, y):
    return x * 10 + y

print reduce(fn, [1, 3, 5, 7, 9])


def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

print 'integer:', reduce(fn, map(char2num, '13579'))


def prod(x, y):
    return x * y

print reduce(prod, [1, 3, 5, 7, 9])


def first2upper(s):
    return s.lower().title()

print map(first2upper, ['adam', 'LISA', 'barT'])
