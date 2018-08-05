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

a = [1, 342, 223, 'India', "Fedora"]
print(a[1::2])
b = len(a)
print(b)

a = ['shiyanlou', 'is', 'powerful']
for x in a:
    print(x, end = ' ')

while True:
    n = int(input("Enter an integer: "))
    if n < 0:
        continue
    elif n == 0:
        break
    print("Square is ", n ** 2)
print("Goodbye!")

for i in range(0, 5):
    print(i)

sticks = 21

print("There are 21 sticks, you can take 1-4 number of sticks at a time.")
print("Whoever will take the last stick will loose")

while True:
    print("Sticks left: " , sticks)
    sticks_taken = int(input("Take sticks(1-4):"))
    if sticks == 1:
        print("You took the last stick, you loose")
        break
    if sticks_taken >= 5 or sticks_taken <= 0:
        print("Wrong choice")
        continue
    print("Computer took: " , (5 - sticks_taken) , "\n")
    sticks -= 5

s = input("Enter a line: ")
print("The number of words in the line are %d" % (len(s.split(" "))))
