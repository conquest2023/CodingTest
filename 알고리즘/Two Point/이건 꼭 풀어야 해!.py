import sys
n,m=map(int,sys.stdin.readline().split())
M=list(map(int,sys.stdin.readline().split()))
M.sort()
for i in range(n-1):
    M[i+1]+=M[i]
for i in range(m):
    A,B=map(int,sys.stdin.readline().split())
    if A==B:
        print(M[A-1]-M[B-2])
        continue
    if A!=1:
        print(M[B-1]-M[A-2])
        continue
    else:
        print(M[B-1])
