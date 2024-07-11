"""N,M=map(int,input().split())
day=[]
start=0
count=0
total=0
dp=[[0]*(N+1) for i in range(M+1)]
for i in range(M):
    A,B=map(int,input().split())
    day.append([A,B])
day=sorted(day)
for i in range(1,M+1):
    day2 = day[i][0]
    page = day[i][1]
    for j in range(1,N+1):
        if j<day2:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-day2]+page)

print(dp[M][N])"""

n, m = map(int, input().split())
dp = [[0] * (n+1) for _ in range(m+1)]
list = [[0,0]]

for _ in range(m) :
  a, b = map(int, input().split())
  list.append([a,b])
list = sorted(list)
for i in range(1, m+1):
  for j in range(1, n+1):
    day, page = list[i][0], list[i][1]
    if j < day:
      dp[i][j] = dp[i-1][j]
    else :
      dp[i][j] = max(dp[i-1][j], dp[i-1][j-day] + page)

print(dp[m][n])