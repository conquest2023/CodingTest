from collections import deque

def BFS(num1,num2):
    count=0
    queue=deque()
    queue.append([num1,num2,count])
    while queue:
        x,y,count=queue.popleft()
        if x<y:
            queue.append([x * 2, y + 3, count + 1])
            queue.append([x + 1, y, count + 1])
        if x==y:
            return print(count)


N=int(input())

for i in range(N):
    A,B=map(int,input().split())
    BFS(A,B)