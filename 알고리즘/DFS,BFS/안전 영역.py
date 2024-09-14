"""from collections import deque

def BFS(x,y,idx2):
    global count
    queue=deque()
    queue.append([x,y])
    visited[x][y]=True
    while queue:
        x,y=queue.popleft()
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(4):
            X=x+dx[i]
            Y=y+dy[i]
            if X>=N or X<0 or Y>=N or Y<0:
                continue
            if  visited[X][Y]==False and Box[X][Y]>idx2:
                visited[X][Y]=True
                queue.append([X,Y])



N=int(input())
ans=[]
Box=[]
Max=0
for a in range(N):
    M=list(map(int,input().split()))
    Box.append(M)
    idx=max(M)
    Max=max(Max,idx)
result=0
for a in range(1,Max):
    visited = [[False] * N for j in range(N)]
    count=0
    for b in range(N):
        for c in range(N):
            if Box[b][c]>a and  visited[b][c]==False:
                BFS(b,c,a)
                count+=1
    if result<count:
        result=count
print(result)"""
from collections import deque

n = int(input())
graph = []
maxNum = 0

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] > maxNum:
            maxNum = graph[i][j]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(a, b, value, visited):
    q = deque()
    q.append((a, b))
    visited[a][b] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] > value and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))


result = 0
for i in range(maxNum):
    visited = [[0] * n for i in range(n)]
    cnt = 0

    for j in range(n):
        for k in range(n):
            if graph[j][k] > i and visited[j][k] == 0:
                bfs(j, k, i, visited)
                cnt += 1

    if result < cnt:
        result = cnt

print(result)