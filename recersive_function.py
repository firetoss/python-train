# -*- coding: utf-8 -*-
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

print fact(1)
print fact(5)
print fact(100)


# 尾递归
# 尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
# 这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，
# 不会出现栈溢出的情况。
def fact1(n):
    return fact_iter(1, 1, n)


def fact_iter(product, count, max):
    if count > max:
        return product
    return fact_iter(product * count, count + 1, max)

print fact1(2)
print fact1(6)
print fact1(99)
