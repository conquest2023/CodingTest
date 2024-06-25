import sys
n,m=map(int,sys.stdin.readline().split())
cnt=list(map(int,sys.stdin.readline().split()))
for i in range(m):
    c,d=map(int,sys.stdin.readline().split())
    print(sum(cnt[c-1:d]))