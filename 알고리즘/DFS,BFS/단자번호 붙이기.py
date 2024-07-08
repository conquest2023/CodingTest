from collections import deque

def bfs(x,y):
    global total
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue=[(x,y)]
    while queue:
        x,y=queue.pop()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if Box[nx][ny]==1:
                total+=1
                Box[nx][ny]=0
                queue.append((nx,ny))
    return total

n=int(input())
count=[]
total=0
Sum=0
Box=[]
for i in range(n):
    a=list(map(int,input()))
    Box.append(a)
    visited = [[False]*n for _ in range(n + 1)]
for i in range(len(Box)):
    for j in range(len(Box)):
       if Box[i][j]==1:
          bfs(i,j)
          if total==0:
              total=1
              count.append(total)
          else:
              count.append(total)
          Sum+=1
          total=0
print(Sum)
count.sort()
for i in count:
    print(i)