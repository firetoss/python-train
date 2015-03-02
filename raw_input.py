# -*- coding: utf-8 -*-
#
# wrong
# birth = raw_input('birth: ')
# right， but do not input character or string
birth = int(raw_input('birth'))

if birth < 2000:
    print '00前'
else:
    print '00后'
