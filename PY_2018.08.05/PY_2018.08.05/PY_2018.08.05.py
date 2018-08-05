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

x = float(input("Enter the value of x: "))
n = term = 1
result = 1.0
while n <= 100:
    term = term * x / n
    result += term
    n += 1
    if term < 0.0001:
        break
print("No of Times = {} and Sum = {}".format(n, result))

print("-" * 50)
i = 1
while i < 11:
    n = 1
    while n < 11:
        print("{:4d}".format(i * n), end = " ")
        n += 1
    i += 1
    print("\n")
print("-" * 50)

row = int(input("Enter the number of rows: "))
n = row
while n >= 0:
    x = "*" * n
    #y = " " * (row - n)
    print(" " * (row - n) + x)
    n -= 1
'''
a = [1, 342, 223, 'India', "Fedora"]
print(a[0:-1])