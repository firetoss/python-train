import re

test_str = 'fafagagagawww.bah3k1h31kdu.cnfafagaga'

reg = re.compile(r'www\.\w+(\.com|\.cn)?')

print reg.findall(test_str)

# print matchs.group()
