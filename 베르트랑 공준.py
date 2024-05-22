"""
import math
def sosu(num):
    count=0
    start = num
    end = num * 2
    if num == 1:
        return 1
    for i in range(start+1,end):
        sum=0
        for j in range(2,int(math.sqrt(end))+1):
            if i%j==0:
                sum+=1
                break
        if sum==0:
           count+=1
    return count
while True:
    count=0
    n=int(input())
    if n==0:
      break
    print(sosu(n))
"""
""" 에라토스테네스의 체"""
check = [0] * 2 + [1] * 246912
for i in range(2, 246913):
    if check[i]:
        for j in range(i * 2, 246913, i):
            check[j] = 0

while True:
    x = int(input())
    if x == 0:
        break
    print(sum(check[x+1:x*2+1]))