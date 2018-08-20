import re

a = 'pytho0python1pythonn2'

r = re.findall('python?', a)
print(r)