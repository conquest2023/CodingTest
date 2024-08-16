N=int(input())
M=list(map(int,input().split()))
K=list(map(int,input().split()))
total=0
Price=K[0]

for i in range(N-1):
    if Price>K[i]:
        Price=K[i]
    total+=(Price*M[i])
print(total)


