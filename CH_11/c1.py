from enum import Enum

class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4

class Common():
    helo = 1
print(VIP.YELLOW)
Common.helo = 2