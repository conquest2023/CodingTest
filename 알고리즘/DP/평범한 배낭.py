"""N,K=map(int,input().split())
Box=[]
cnt=[[0] *(K+1) for i in range(N+1)]
for i in range(N):
    W,V=map(int,input().split())
    Box.append([W,V])
Box.sort()
Values=0
for i in range(N):
    weight=Box[i][0]
    values=Box[i][1]
    for j in range(1,K+1):
        if  j<weight:
            cnt[i][j]=cnt[i-1][j]
        else:
            cnt[i][j]=max(cnt[i-1][j],cnt[i-1][j-weight]+values)
            #Box[i][0]
            Values=cnt[i][j]
print(Values)
"""


N, K = map(int, input().split())
items = []
for _ in range(N):
    w, v = map(int, input().split())
    items.append((w, v))
dp = [0 for _ in range(K + 1)]
for item in items:
    w, v = item
    for i in range(K, w - 1, -1):
        dp[i] = max(dp[i], dp[i - w] + v)
print(dp[-1])