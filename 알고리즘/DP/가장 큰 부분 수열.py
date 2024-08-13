N=int(input())
M=list(map(int,input().split()))
dp=M

for i in range(1,N):
    count=M[i]
    for j in range(i):
        if M[j]<M[i]:
            dp[i]=max(dp[i],count+dp[j])


print(max(dp))

