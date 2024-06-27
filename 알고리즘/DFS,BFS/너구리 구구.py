import sys
sys.setrecursionlimit(10**9)
def DFS(num,graph,visited,dist):
    global count
    visited[num] = True
    for a,b in graph[num]:
        if not visited[a]:
            count=max(count,dist+b)
            DFS(a,graph,visited,dist+b)
n=int(input())
graph=[[] for i in range(n+1)]
count=0
for i in range(n-1):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
visited=[False]*(n+1)
for a in range(1,len(graph)):
    DFS(a,graph,visited,0)
print(count)
