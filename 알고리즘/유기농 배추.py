n=int(input())
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def BFS(x,y):
    queue=[(x,y)]
    visited[x][y]=0

    while queue:
        x,y=queue.pop(0)

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx<0 or nx>=A or ny < 0 or ny >=B:
                continue
            if visited[nx][ny]==1:
                queue.append((nx,ny))
                visited[nx][ny]=0


for i in range(n):
    A, B, C = map(int, input().split())
    visited=[[0]*(B) for _ in range(A)]
    cnt=0
    for j in range(C):
        x,y=map(int,input().split())
        visited[x][y]=1

    for a in range(A):
        for b in range(B):
            if visited[a][b]==1:
                BFS(a,b)
                cnt+=1
    print(cnt)
"""import sys
sys.setrecursionlimit(10000) # 재귀 깊이 설정

T = int(sys.stdin.readline()) # 테스트 케이스 받는 부분

dx = [-1, 1, 0, 0] # 상하좌우 이동하여 계산하기 위한 list
dy = [0, 0, -1, 1]

def dfs(x, y):
  if x <= -1 or x >= N or y<= -1 or y>= M:
    return False

  if graph[x][y] == 1:
    graph[x][y] = 0

    for i in range(4):
      dfs(x + dx[i], y+dy[i])

    return True
  return False

answer = []
for _ in range(T):
  M, N, K = list(map(int, sys.stdin.readline().split()))  

  graph = [[0]*M for _ in range(N)]

  for _ in range(K):
    x, y = map(int, input().split())
    graph[y][x] = 1

  cnt = 0
  for i in range(N):
    for j in range(M):
      if dfs(i, j):
        cnt +=1

  print(cnt)"""