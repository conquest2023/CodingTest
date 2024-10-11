N,M=map(int,input().split())
total=0
idx=[]
for i in range(N):
    coin=int(input())
    idx.append(coin)
total=M
for i in range(N-1):
    j=i+1
    if idx[i]<idx[j]:
        total=idx[j]*(total//idx[i])+(total%idx[i])

if total==0:
    print(M)
else:
    print(total)

