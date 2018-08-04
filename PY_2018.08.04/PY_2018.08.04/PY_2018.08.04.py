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
