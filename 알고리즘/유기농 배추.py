def dfs(graph,v,visited):
    if len(width)==1:
        return print(1)
    visited[v]=True
    print(v,end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

N=int(input())
width=[]
while True:
    A,B,C=map(int,input().split())
    for i in range(C):
        num0, num1 = map(int, input().split())
        width.append([num0, num1])
    visited=[False]
    dfs(width,1,visited)
    N-=1
    if N==0:
       break
