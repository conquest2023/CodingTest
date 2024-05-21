import math

def sosu(num):
    if num == 0 or num== 1:
        return False
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            return False
    return True

n=int(input())
for i in range(n):
    m=int(input())
    while True:
        if sosu(m):
           print(m)
           break
        else:
            m+=1
