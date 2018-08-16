# d = 1, 2, 3
# a, b, c = d
# print(a, b, c)
# def demo(*param):
#     print(param)

# a = (1,2,3,4,5)
# demo(*a)
def squsum(*param):
    sum = 0
    for i in param:
        sum += i * i
    print(sum)

squsum(1, 2, 3, 4, 5, 6)    