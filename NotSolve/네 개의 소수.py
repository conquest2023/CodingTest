from itertools import combinations, permutations,product
import math
def sosu(num):
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            return False
    return num
cnt=[]
ans=[]
solve=[]
n=int(input())
for i in range(2,int(n//3)+2):
    if sosu(i):
       cnt.append(sosu(i))
for i in product(cnt,repeat=4):
    if sum(i)==n:
        ans.append(i)
if len(ans)==0:
    print(-1)
else:
    idx = ans[-1]
    for i in idx:
        solve.append(i)
    solve.sort()
    for i in solve:
        print(i, end=' ')