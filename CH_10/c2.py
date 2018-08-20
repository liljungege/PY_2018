import re
a = 'c6c++9Java5c#8python'

e = re.findall('python', a,)
if len(e) != 0:
    print ("字符串中包含python")

