# -*- coding: utf-8 -*-
#
from collections import Iterable
import os

print isinstance('abc', Iterable)
print isinstance([1, 2, 3], Iterable)
print isinstance(13, Iterable)

l = ['h', 'y', 'z']
print l[0:2]

for i, value in enumerate([1, 2, 3]):
    print i, value

l = range(100)
print l

# 前10个
print l[:10]
# 后10个
print l[-10:]
# 前11-20个
print l[10:20]

# 前10个，每2个取1个
print l[:10:2]

print [x * x for x in range(1, 11)]

print [x * x for x in range(1, 11) if x % 2 == 0]

print [m + n for m in 'abc' for n in 'xyz']

print [d for d in os.listdir('.')]

# generator
g = (x * x for x in range(10))
print g
print g.next()
