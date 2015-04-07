# -*- coding: utf-8 -*-
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
print fib(6)


def odd():
    print 'step 1'
    yield 1
    print 'step 2'
    yield 3
    print 'step 3'
    yield 5
o = odd()
o.next()
o.next()
o.next()
