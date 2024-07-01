"""from collections import deque

def BFS(start):
    queue=deque([start])
    visited[start]=1
    while queue:
        v=queue.popleft()
        for i in cnt[v]:
            if not visited[i]:
                visited[i]+=visited[v]+1
                queue.append(i)

N,M=map(int,input().split())
cnt=[[] for i in range(N+1)]
count=0
total=[]
for _ in range(N):
    A,B=map(int,input().split())
    cnt[A].append(B)
    cnt[B].append(A)
for i in range(1,N+1):
    visited = [0] * (N + 1)
    BFS(i)
    total.append(sum(visited))
print(total)"""



from collections import deque
def bfs(graph, start):
    num = [0] * (n+1)
    visited = [start]
    queue = deque()
    queue.append(start)
    while queue:
        a = queue.popleft()
        for i in graph[a]:
            if i not in visited:
                num[i] = num[a] + 1
                visited.append(i)
                queue.append(i)
    return sum(num)
n, m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
result = []
for i in range(1, n+1):
    result.append(bfs(graph, i))
print(result.index(min(result))+1)



