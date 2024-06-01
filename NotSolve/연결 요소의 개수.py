import sys
N,E=map(int,sys.stdin.readline().split())
Box=[[] for _ in range(N+1)]
visited=[False]*(N+1)
def dfs(v):
    visited[v]=True
    for i in Box[v]:
        if not visited[i]:
           dfs(i)
for i in range(E):
    n,m=map(int,sys.stdin.readline().split())
    Box[n].append(m)
    Box[m].append(n)
count=0
for i in range(1,N+1):
    if visited[i]==False:
        dfs(i)
        count += 1

print(count)