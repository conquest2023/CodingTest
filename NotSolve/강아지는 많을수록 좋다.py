import sys
from collections import deque

def BFS(N):
    queue=deque()
    queue.append(N)
    while queue:
        N = queue.popleft()
        if N==0:
           return dp
        for i in (N-A,N-B):
            if i >=0:
              if visited[i]:
                  continue
              else:
                  queue.append(i)
                  dp[i]=dp[N]+1
                  visited[i]=True



N,M,A,B=map(int,sys.stdin.readline().split())
dp =[0] * (N+1)
dp[N]=0
visited=[False]*(N+1)
for i in range(M):
    L,R=map(int,sys.stdin.readline().split())
    for j in range(L,R+1):
        visited[j]=True
BFS(N)
if dp[0]:
    print(dp[0])
else:
    print(-1)