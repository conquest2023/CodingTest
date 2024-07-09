"""n=int(input())
Box=[]
for i in range(n):
    T,P=map(int,input().split())
    Box.append([T,P])
count=0
total=[]
start=0
while start>=n:
    for i in range(start,n):
        count += Box[start][1]
        start+=Box[start][0]
total.append(count)
print(total)"""
n=int(input())
Box=[]
dp=[0 for i in range(n+1)]
for i in range(n):
    T,P=map(int,input().split())
    Box.append([T,P])
count=0
total=[]
start=0
for i in range(n):
    for j in range(i+Box[i][0],n+1):
      if  dp[j]<dp[i]+Box[i][1]:
          dp[j]=dp[i]+Box[i][1]
print(dp[-1])
"""Top-Down"""
n=int(input())
Box=[]
dp=[0 for i in range(n+1)]
for i in range(n):
    T,P=map(int,input().split())
    Box.append([T,P])
count=0
total=[]
start=0
for i in range(n-1,-1,-1):
    if i+Box[i][0]>n+1:
        dp[i]=dp[i+1]
    else:
        dp[i]=max(dp[i+1],+dp[i+Box[i][0]]+Box[i][1])


