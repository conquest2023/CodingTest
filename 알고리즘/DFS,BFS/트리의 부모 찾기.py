import sys
input=sys.stdin.readline
sys.setrecursionlimit(1000000)

def DFS(i):
    for v in graph[i]:
        if cnt[v]==0:
            cnt[v]=i
            DFS(v)
    return
n=int(input())
graph=[[] for i in range(n+1)]
cnt=[0]*(n+1)
for i in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

DFS(1)

for i in range(2,(n+1)):
    print(cnt[i])