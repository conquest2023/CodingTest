from collections import deque

D=deque()

n=int(input())
m=list(map(int,input().split()))
m=deque(m)
cnt=0
rank=0
for i in range(len(m)):
    while True:
        cnt+=1
        m.popleft()
