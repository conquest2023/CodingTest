N=int(input())
Boxs=list(map(int,input().split()))
dp=[1]*(N+1)
total=0
for i in range(N):
    for j in range(i):
            if Boxs[i]>Boxs[j]:
                dp[i]=max(dp[i],dp[j]+1)
print(max(dp))


