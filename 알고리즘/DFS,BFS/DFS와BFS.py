from collections import deque
A,B,C=map(int,input().split())
cnt=[[] for _ in range(A+1)]
for i in range(B):
    num1,num2=map(int,input().split())
    cnt[num1].append(num2)
    cnt[num2].append(num1)
print(cnt)
for i in range(A+1):
    cnt[i].sort()
def dfs(v):
    print(v, end=' ')
    visited[v]=True
    for i in cnt[v]:
       if not visited[i]:
           dfs(i)
visited=[False]*(A+1)
dfs(C)
def bfs(v):
    queue=deque()
    queue.append(v)
    visited[v]=True
    while queue:
        Now=queue.popleft()
        print(Now,end=' ')
        for i in cnt[Now]:
            if not visited[i]:
                visited[i]=True
                queue.append(i)
print()
visited=[False]*(A+1)
bfs(C)


