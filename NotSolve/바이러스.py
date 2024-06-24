N=int(input())
E=int(input())
cnt=[[] for  _ in range(N+1)]
count=0
cnt2=[]
for i in range(E):
    A,B=map(int,input().split())
    cnt[A].append(B)
    cnt[B].append(A)

visited=[False]*(N+1)
def DFS(v):
    global count
    visited[v]=True
    count+=1
    for i in cnt[v]:
        if not visited[i]:
            cnt2.append(i)
            DFS(i)


DFS(1)
print(count-1)