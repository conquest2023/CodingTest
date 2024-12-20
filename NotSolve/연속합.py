# import sys
# n=int(sys.stdin.readline())
# m=list(map(int,sys.stdin.readline().split()))
# dp=[-1]*(n+1)
# for i in range(n):
#     for j in range(n-i):
#         dp[j]=max(m[i]+dp[j],m[i])
# print(max(dp))

n = int(input())
m = list(map(int, input().split(' ')))

for i in range(1, n):
    m[i] = max(m[i], m[i] + m[i - 1])

print(max(m))
### 메모이제이션###