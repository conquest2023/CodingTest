from collections import deque

rank=0
n=int(input())
cnt=[]
m=list(map(int,input().split()))
m=deque(m)
m2=[i for i in range(1,n+1)]

for i in m:
    print(m2[0])
    m2.pop(0)
    rank=i
    while rank!=0:
        if rank>0:
           cnt.append(m.popleft())
           rank-=1

        if rank<0:
           rank+=1