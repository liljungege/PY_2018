import re
s = 'abc, acc, adc, aec, afc, ahc'

r = re.findall('\w', s)
print(r)