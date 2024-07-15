from collections import deque
def BFS(x,y):
    global ans
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue=[(x,y)]
    target=cnt[x][y]
    while queue:
        x,y=queue.pop(0)
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx >=n or nx<0 or ny>=n or ny<0:
                continue
            if  cnt[nx][ny]>target:
                cnt[nx][ny]=0
                queue.append((nx,ny))
                ans+=1
    return


Max_count=0
ans=0
n=int(input())
cnt=[]
Max=0
for i in range(n):
    cnt.append(list(map(int,input().split())))
    Max=max(cnt)
for i in range(n):
    for j in range(n):
        BFS(i,j)
        Max_count=max(Max_count,ans)
print(Max_count)


