N=int(input())
M=list(map(int,input().split()))
dp=[1]*N
for i in range(1,N):
    for j in range(i):
        if M[j]<M[i]:
            dp[i]=max(dp[i],dp[j]+1)

print(max(dp))