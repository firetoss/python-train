# -*- coding: utf-8 -*-

# def my_abs(x):
#     if not isinstance(x, (int, float)):
#         raise TypeError('bad operand type')

#     if x >= 0:
#         return x
#     else:
#         return -x

# my_abs('a')

import math


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.cos(angle)

    return nx, ny
x, y = move(100, 100, 60, math.pi / 6)
print x, y

# 实际返回的事一个tuple
r = move(100, 100, 60, math.pi / 6)
print r


def func(arg=None):
    if arg is None:
        return []
    arg.append('end')
    return arg

print func(['is'])


# 可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum += n
    return sum

print calc(1, 2)

# 参数为list或tuple
l = [1, 2]
t = (1, 2)
print calc(*l)
print calc(*t)


# 关键字参数
# 关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
def person(name, age, **kw):
    print 'name: ', name, 'age: ', age, 'other: ', kw

person('hyz', 31)
person('hyz', 31, city='bj', job='coder')

d = {'city': 'bj', 'job': 'coder'}
person('hyz', 31, **d)


# 在Python中定义函数，可以用必选参数、默认参数、可变参数和关键字参数，
# 这4种参数都可以一起使用，或者只用其中某些，但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数和关键字参数
def multi_args(a, b, c=0, *args, **kw):
    print 'a=', a, 'b=', b, 'c=', c, 'args=', args, 'kw=', kw

multi_args(1, 2)
multi_args(1, 2, 3)
multi_args(1, 2, 3, 4, 5)
multi_args(1, 2, 3, 4, 5, other=6)

args = (1, 2, 3, 4)
kw = {'other': 6}
multi_args(*args, **kw)
