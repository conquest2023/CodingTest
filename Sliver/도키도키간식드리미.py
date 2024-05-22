""" 내가 푼 코드
from collections import deque
rank=0
n=int(input())
cnt=[]
m=list(map(int,input().split()))
m=deque(m)
target=1
while True:
    if n==0:
       break
    dump=m.popleft()
    if dump==target:
        target+=1
        pass
    else:
        cnt.append(dump)
    n-=1


m2=[i for i in range(cnt[-1],max(cnt)+1)]
m2=sorted(m2,reverse=True)
if cnt==m2:
    print("Nice")
else:
    print("Sad")
    """
"""개선"""
from collections import deque

N = int(input())
queue = deque(map(int, input().split()))
stack = deque()
i = 1
while queue:
    if queue and queue[0] == i:
        queue.popleft()
        i += 1
    else:
        stack.append(queue.popleft())
    while stack and stack[-1] == i:
        stack.pop()
        i += 1

print("Nice" if not stack else "Sad")