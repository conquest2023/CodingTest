import sys
N=int(sys.stdin.readline())
dp=[1,2,4,7]
for i in range(4,1000001):
    dp.append((sum(dp[i-3:])) % 1000000009)
for i in range(N):
    M=int(sys.stdin.readline())
    print(dp[M-1] % 1000000009)