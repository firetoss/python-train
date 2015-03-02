# -*- coding: utf-8 -*-
# dict内部存放的顺序和key放入的顺序是没有关系的
d = {'h': 1, 'y': 2, 'z': 3}

print d['y']

print 'a' in d

print d.get('z')
print d.get('a')

d['s'] = 4

print '====================='
t = (5,)
d[t] = 5

print d
print '====================='

# 遍历方法
for key in d:
    print "key: %s" % key, d[key]

for (key, value) in d.items():
    print "key: %s" % key, value

for key, value in d.iteritems():
    print "key: %s" % key, value

for key, value in zip(d.iterkeys(), d.itervalues()):
    print "key: %s" % key, value
# 注意：
# dict与list相比有如下特点：
#     1. 查找和插入速度快
#     2. 占用内存多
# dict的key必须为不可变的
