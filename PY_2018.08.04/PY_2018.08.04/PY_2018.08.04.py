import math
print(math.e)
print("shiyanyou")
print("shiyanlou's best")
print('shiyanlou\'s best')

number = int(input("Enterr an interger: "))
if number <= 100:
    print("Your number is smaller than equal to 100")
else:
    print("Your number is greater than 100")

amount = float(input("Enter amount: ")) # input data
inrate = float(input("Enter Interrest rate: ")) # input inrate
period = int(input("Enter period: ")) # input period
value = 0
year = 1
while year <= period:
    value = amount + (inrate * amount)
    print("Year {} Rs. {:.2f}".format(year, value))
    amount = value
    year  = year + 1

N = 10
sum = 0
count = 0
print("Please input 10 numbers:")
while count < N:
    number = float(input())
    sum = sum + number
    count = count + 1
avg = sum / N
print("N = {}, Sum = {}".format(N, sum))
print("Average = {:.2f}".format(avg))

fahrenheit = 0
print("Fahrenheit Celsius")
while fahrenheit <= 250:
    celsius = (fahrenheit - 32) / 1.8
    print("{:5d} {:7.2f}".format(fahrenheit, celsius))
    fahrenheit = fahrenheit + 25

days = int(input("Enter days: "))
months = days // 30
days = days % 30
print("Months = {} Days = {}".format(months, days))
days = int(input("Enter days: "))
print("Months = {} Days = {}".format(*divmod(days, 30)))

N = 100
a = 2
while a < N:
    print(str(a))
    a *= a

sum = 0
for i in range(1, 11):
    sum += 1.0 / i;
    print("{:2d} {:6.4f}".format(i, sum))

import math
circle_radius = 2
circle_square = circle_radius * circle_radius * math.pi
print("{:.10f}".format(circle_square))

