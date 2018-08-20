import re 

qq = '100001'
# 4 ~ 8
r = re.findall('^\d{4,8}$', qq)
print(r)