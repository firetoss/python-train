# -*- coding: utf-8 -*-
age = 20
if age > 18:
    print 'your age is %d' % age
    print 'adult'

age = 3
if age > 18:
    print 'your age is %d' % age
    print 'adult'
elif age >= 6:
    print 'teenger'
else:
    print 'kid'

v = [1]
if v:
    print True

v = (1,)
if v:
    print True

v = 1
if v:
    print True

v = 'h'
if v:
    print True

v = None
if not v:
    print False

v = []
if not v:
    print False

v = 0
if not v:
    print False

v = ''
if not v:
    print False
