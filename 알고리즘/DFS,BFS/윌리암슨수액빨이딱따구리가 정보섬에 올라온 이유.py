import sys
sys.setrecursionlimit(10**7)
from collections import deque
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def BFS(x,y,dis):

    queue=deque()
    queue.append([x,y,dis])
    while queue:
        x,y,dis=queue.popleft()
        dis+= 1
        for i in range(4):
            X=x+dx[i]
            Y=y+dy[i]
            if X>=N or X<0 or Y>=N or Y<0:
                  continue
            if Box[X][Y]==1:
                continue
            if Box[X][Y] in [3,4,5]:
                  print("TAK")
                  print(dis)
                  exit()
            Box[X][Y] =1
            queue.append([X, Y,dis])


N,M=map(int,input().split())
target=[]
count=0
Box=[]
visited=[[False] * N for i in range(1,N+1)]
Box=[list(map(int, list(input()))) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if Box[i][j]==2:
           BFS(i,j,0)
           break

print("NIE")
"""
import sys
from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

n, m = map(int, sys.stdin.readline().split())  # 행,열
graph = [list(map(int, list(input()))) for _ in range(n)]

dq = deque()  

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            dq.append((i, j, 0))   # 딱따구리 위치, 거리
            graph[i][j] = 1        # 방문 표시, 장애물로 변경 

while dq:
    x, y, dis = dq.popleft()
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if graph[nx][ny] == 1:   # 방문한 경우 or 장애물
            continue
        if graph[nx][ny] in [3, 4, 5]: # 음식인 경우 그만 
            print("TAK") 
            print(dis + 1)
            exit()
        dq.append((nx, ny, dis + 1))
        graph[nx][ny] = 1

print("NIE")
"""

