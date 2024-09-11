"""N=int(input())
lines=list(map(int,input().split()))
count=0
num=0
dp=[0]*N
for i in lines:
    num+=1
    if  max(dp)>=N:
        break
    for j in range(num-1,N):
        dp[j]=max(lines[j],lines[j]+j)
        if dp[j]==lines[j]+j:
            count+=1
        break

if max(dp)<N:
    print(-1)
else:
    print(dp)
    print(count)
"""
import sys

n = int(input())
jump = list(map(int, sys.stdin.readline().split()))
dp = [n + 1] * n
dp[0] = 0

for i in range(n):
	for j in range(1, jump[i] + 1):
		if i + j < n:
			dp[i + j] = min(dp[i] + 1, dp[i + j])

if dp[n - 1] == n + 1:
	print(-1)
else:
	print(dp[n - 1])