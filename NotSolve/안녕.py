N=int(input())
M=list(map(int,input().split()))
lines=list(map(int,input().split()))

dp=[0]*(N+1)

for i in range(N):
    energy=0
    for j in range(i):
         if M[j]<100:
            dp[i]=max(dp[i],dp[j]+lines[j])

print(dp)