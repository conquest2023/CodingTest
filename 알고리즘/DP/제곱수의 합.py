
"""n=int(input())
Dp=[0]*n
count=0
total=n
for i in range(n,0,-1):
    if total==i*i:
       total-=i*i
       count+=1
       break
    if total-i*i>0:
       total-=i*i
       count+=1

print(total+count)
"""
import sys
input = sys.stdin.readline

n = int(input())
dp = [k for k in range(n+1)]

for i in range(1, n + 1):
    for j in range(1, i):
        if j*j > i:
            break
        if dp[i] > dp[i-j*j]+1:

            dp[i] = dp[i-j*j] + 1
print(dp[n])


