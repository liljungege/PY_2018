'''
def palindrom(s):
    return s == s[::-1]
if __name__ == '__main__':
    s = input("Enter a string: ")
    if palindrom(s):
        print("Yay a palindrome")
    else:
        print("Oh no, not a palidrome")

def palindrom(s):
    return s == s[::-1]
s = input("Enter a string: ")
if palindrom(s):
    print("Yay a palindrome")
else:
    print("Oh no, not a palidrome")

def change():
    global a
    a = 90
    print(a)
a = 9
print(a)
change()
print(a)

def func(a, b=5, c=10):
    print("a is", a, "and b is", b, "and c is", c)
func(12, 23, 23)
def hello(*, name = 'user'):
    print("Hello", name)
print(hello(name = 'shiyanlou'))

import math

def longest_side(a, b):
    """
    Function to find the length of the longest side of a right triangle.
    :arg a: Side a of the triangle
    :arg b: Side b of the triangle
    
    :return: Length of the longest side c as float
    """
    return math.sqrt(a*a + b*b)
if __name__ == '__main__':
    print(longest_side.__doc__)
    print(longest_side(4, 5))

def high(func, value):
    return func(value)
lst = high(dir, int)
print(lst[-3:])

lst = [1, 2, 3, 4, 5]
def square(num):
    return num ** 2
print(list(map(square, lst)))
'''
fobj = open("s.txt")
print(fobj)