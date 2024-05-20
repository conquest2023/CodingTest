from collections import deque
n=int(input())
rank=0
count=1
queue=deque()
cnt=[]
number=[i for i in range(1,n+1)]
m=list(map(int,input().split()))
for i in m:
    rank=i
    if count==1:
       queue.append(number[0])
    count+=1
    while rank!=i:

print(queue)
