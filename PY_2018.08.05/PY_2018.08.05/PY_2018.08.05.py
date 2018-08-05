'''
number = int(input("Enter a number: "))
if number < 100:
    print("The number is less than 100")
else:
    print("The number is greater than 100")

x = int(input("Please enter an integer: "))
if x < 0:
    x = 0
    print("Negetive changed to zero")
elif x == 0:
    print("zero")
elif x:
    print("Single")
else:
    print("More")

a, b = 0, 1
while b < 100:
    print(b, end = ' ')
    a, b = b, a + b
'''
x = int(input("Enter the value of x: "))
while