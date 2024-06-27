
"""def bfs(x,y,count,cnt):
    queue=[(x,y)]
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    while queue:
        x,y=queue.pop(0)
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=5 and ny<0 or ny>=5:
                continue
            elif cnt[nx][ny]==1:
                 count-=1
                 cnt[nx][ny]=0
                 print(nx,ny)
                 queue.append((nx,ny))
            elif cnt[nx][ny]==-1:
                 pass
    return count"""
def dfs(x,y,cnt,count,time):
    if count <= 0:
        print(1)
        exit(0)
    if time==0:
        return
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=5 or ny<0 or ny>=5:
                continue
            if cnt[nx][ny] == 1:
                cnt[nx][ny]=-1
                dfs(nx,ny,cnt,count-1,time-1)
                cnt[nx][ny]=1
            elif cnt[nx][ny]==0:
                 cnt[nx][ny]=-1
                 dfs(nx,ny,cnt,count,time-1)
                 cnt[nx][ny]=0
n=5
cnt=[list(map(int,input().split()))  for _ in range(n)]
#visited = [[0] * (n+1) for _ in range(n+1)]
#for i in range(n):
#   pos=[[list(map(int,input().split()))]]
#  cnt.append(pos)
x,y=map(int,input().split())
count=2
if cnt[x][y]==1:
    count-=1
cnt[x][y] = -1
time = 3
dfs(x,y,cnt,count,time)
print(0)