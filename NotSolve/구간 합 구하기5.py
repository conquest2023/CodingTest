"""import sys
col,row=map(int,sys.stdin.readline().split())
cnt=[]
for i in range(col):
    pos=list(map(int,sys.stdin.readline().split()))
    cnt.append(pos)
for i in range(1,len(cnt)):
    cnt[i][0]+=cnt[i-1][0]
    cnt[0][i]+=cnt[0][i-1]
for i in range(1,len(cnt)):
    for j in range(1,len(cnt)):
        cnt[i][j]=cnt[i][j]-cnt[i-1][j-1]+cnt[i][j-1]+cnt[i-1][j]
for i in range(row):
    x1,y1,x2,y2=map(int,sys.stdin.readline().split())
    print(cnt[x2-1][y2-1]-cnt[x1-1][y2-1]-cnt[x2-1][y1-1]+cnt[x1-1][y1-1])"""
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
A=[[0]*(n+1)]
D=[[0]*(n+1) for _ in range(n+1)]
for i in range(n):
    A_row=[0]+[int(x) for x in input().split()]
    A.append(A_row)
for i in range(n+1):
    for j in range(1,n+1):
        D[i][j]=D[i][j-1]+D[i-1][j]-D[i-1][j-1]+A[i][j]
for _ in range(m):
    x1, y1, x2, y2 = map(int,input().split())
    print(D[x2][y2]-D[x1 -1][y2]-D[x2][y1 - 1] + D[x1 - 1][y1 - 1])


