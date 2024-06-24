from collections import deque
a,b=map(int,input().split())

cnt=[i for i in range(1,a+1)]
queue=deque(cnt)
queue2=[]
while len(queue)!=0:
    count=0
    for i in range(b):
       count+=1
       if count==b:
            queue2.append(str(queue.popleft()))
       else:
            front=queue.popleft()
            queue.append(front)

print("<",', '.join(queue2),">", sep="")