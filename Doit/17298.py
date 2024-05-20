from collections import deque

n=int(input())
m=list(map(int,input().split()))
cnt=[]
cnt2=[1]
D = deque(m)

while True:
    if len(D)==0:
        break

    f=D.popleft()
    cnt.append(f)
    if cnt[-1]==1:
       cnt.pop(-1)
    elif cnt[-1]==cnt2[0]+1:
        cnt2.pop(0)
        g=cnt.pop(-1)
        cnt2.append(g)
if