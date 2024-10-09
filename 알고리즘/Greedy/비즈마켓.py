import sys
N,M=map(int,sys.stdin.readline().split())
A=list(map(int,sys.stdin.readline().split()))
B=list(map(int,sys.stdin.readline().split()))

A.sort(reverse=True)
B.sort()
count=0
for i in range(N):
    if i>=len(B):
        break
    if A[i]-B[i]>0:
        count+=A[i]-B[i]

print(count)
