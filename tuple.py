# -*- coding: utf-8 -*-
# tuple demo
# 有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
# 没有append()，insert()这样的方法。其他获取元素的方法和list是一样的，
# 你可以正常地使用classmates[0]，classmates[-1]，但不能赋值成另外的元素。
classmates = ('h', 'y', 'z')

# tuple定义时需要注意
t = (1, 2)
print 'is a tuple', t

t = ()
print 'is a tuple', t

t = (1)
print 'is not a tuple', t

t = (1,)
print 'is a tuple', t

# 可变的tuple
t = (1, 2, ['x', 'y'], 3)
t[2][0] = 'h'
t[2][1] = 'y'
t[2].append('z')
print t
