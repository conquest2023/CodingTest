import math,itertools
from itertools import permutations
def sosu(total):
    for i in range(2,int(math.sqrt(total))+1):
        if total%i==0:
            return 0
    return 1

N,M=map(int,input().split())
weight=list(map(int,input().split()))
cnt=[]
data=itertools.permutations(weight,M)
for i in data:
    total=sum(i)
    if sosu(total):
        if total not in cnt:
            cnt.append(total)
cnt.sort()
if len(cnt)==0:
    print(-1)
else:
    for i in cnt:
        print(i,end=' ')
"""
for i in range(len(weight)):
    for j in range(i+1,len(weight)):
        for z in range(j+1,len(weight)):
            total=weight[i]+weight[j]+weight[z]
            if sosu(total):
                if total not in cnt:
                    cnt.append(total)"""