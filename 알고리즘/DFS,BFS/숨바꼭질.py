from collections import deque
def BFS(num):
    queue=deque([num])
    while True:
        x = queue.popleft()
        if x==m:
           return visited[x]
        for i in (x-1,x+1,x*2):
            if  0<=i< MAX and not visited[i]:
                visited[i]=visited[x]+1
                queue.append(i)



MAX=100001
visited = [0] * MAX
n,m=map(int,input().split())
count=0
print(BFS(n))

