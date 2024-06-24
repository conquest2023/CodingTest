n=int(input())
A=list(map(int,input().split()))
A.sort(reverse=True)
S=list(map(int,input().split()))
S.sort()
total=0
for i in range(n):
    total+=A[i]*S[i]
print(total)

