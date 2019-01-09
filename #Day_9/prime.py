import math
def is_prime1(num):
    if num < 2:
        return "Prime"
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0:
            return False
        else:
            return True
