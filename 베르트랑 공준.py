import math
def sosu(num):
    count=0
    start = num
    end = num * 2
    if num == 1:
        return 1
    for i in range(start+1,end):
        for j in range(2,int(math.sqrt(end))+1):
            if i%j==0:
                break
        count+=1
    return count
while True:
    n=int(input())
    if n==0:
        break
    print(sosu(n))