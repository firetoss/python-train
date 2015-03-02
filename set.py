# -*- coding: utf-8 -*-
s = set([1, 2, 3])
print s

# 添加key
s.add(4)
print s

# 删除key
s.remove(4)
print s

s1 = set([2, 3, 4])
# 两个set的交集
print s & s1

# 两个set的并集
print s | s1

# 可变对象无法添加至set中
# l = [1, 2]
# s.add(l)

# tuple不可变，所以可添加至set中
t = (5,)
s.add(t)
print s

# list为可变的，所以不可添加到set中
# t = (5, [6, 7])
# s.add(t)
