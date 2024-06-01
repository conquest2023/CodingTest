from collections import deque
n=int(input())
stack=[i for i in range(1,n+1)]
queue=deque(stack)
cnt=[]
while n!=0:
     ban=queue.popleft()
     cnt.append(ban)
     if len(queue)==0:
         break
     ban2=queue.popleft()
     queue.append(ban2)

     n-=1

for i in cnt:
    print(i,end=' ')