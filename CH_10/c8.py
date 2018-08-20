import re

def convert(value):
    matched = value.group()
    return '!!' + matched + '!!'

language = 'PythonC#JavaPHP'
r = re.sub('C#', convert, language, 0)
print(r)


    