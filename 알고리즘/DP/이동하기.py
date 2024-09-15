
N,M=map(int,input().split())
Boxs=[]
dp=[[0]*  (M+1) for i in range(N+1)]
for i in range(N):
    Boxs.append(list(map(int,input().split())))
for a in range(1,N+1):
    for b in range(1,M+1):
        dp[a][b]=max(dp[a-1][b],dp[a][b-1],dp[a-1][b-1])+Boxs[a-1][b-1]
print(dp)