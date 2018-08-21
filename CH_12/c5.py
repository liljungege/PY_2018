import re
list_x = [1, 0, 1, 0, 0, 1]
list_u = ['a', 'B', 'x', 'D']
r = filter(lambda x: True if x in re.findall('[A-Z]', x) else False, list_u)
# z = filter(lambda x: )
print(list(r))
