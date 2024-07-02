def DP(N,dp):
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    if N<=3:
      return dp[N]
    else:
        for i in  range(4,N+1):
            dp[i]=dp[i-3]+dp[i-2]
    return dp[N]
n=int(input())
dp=[0]*101
for i in range(n):
     m=int(input())
     print(DP(m,dp))

"""다른 코드
import sys
input = sys.stdin.readline
arr = [0, 1, 1, 1] + [0 for x in range(97)]

def func(x):
  if arr[x]:
    return arr[x]
  else:
    arr[x] = func(x-2) + func(x-3)
    return arr[x]

t = int(input())
for _ in range(t):
  n = int(input())
  print(func(n))"""