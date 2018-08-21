from enum import Enum

class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4

class VIP1(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4

# result = VIP.GREEN == VIP1.GREEN
# result1 = VIP.GREEN is VIP.GREEN
# print(result)
# print(result1)
a = 1
print(VIP(a))