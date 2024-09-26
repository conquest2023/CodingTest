"""N,M=map(int,input().split())
coin=[]
dp=[]
for i in range(N):
    coin.append(int(input()))

for i in coin:
    if M%i==0:
       dp.append(M//i)
    else:
        for j in coin:
            if (M%i)%j==0:
                dp.append(((M%i)//j)+M//i)
if len(dp)==0:
    print(-1)
else:
    print(min(dp))
"""
from sys import stdin

n, k = map(int, stdin.readline().split())

li =[]

for i in range(n):
   li.append(int(stdin.readline().rstrip()))

dp = [10001] * (k+1)
dp[0] = 0

for num in li:
   for i in range(num, k+1):
       dp[i] = min(dp[i],dp[i-num]+1)
if dp[k] == 10001:
   print(-1)
else:
   print(dp[k])