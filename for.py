# -*- coding: utf-8 -*-
names = ['h', 'y', 'z']
for name in names:
    print name

sum = 0
for x in xrange(1, 10):
    sum += x
print sum

print range(5)

sum = 0
n = 100
while n > 0:
    sum += n
    n -= 2
print sum

# 列表生成式
L = ['Hello', 'World', 18, 'Apple', None]
print [s.lower() for s in L if isinstance(s, str)]
