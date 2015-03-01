# -*- coding: utf-8 -*-
classmates = ['h', 'y', 'z']
print classmates

print len(classmates)

# 按照索引打印list中得值
print classmates[0]
print classmates[-1]

# 在list最后追加
classmates.append('h')
print classmates

# 指定索引位置插入
classmates.insert(1, 'zz')
print classmates

# 弹出list中最后一位索引的值
print 'pop: %s' % classmates.pop()
print classmates

# 弹出list中指定索引的值
print 'pop: %s' % classmates.pop(1)
print classmates
