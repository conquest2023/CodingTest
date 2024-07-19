N,M=map(int,input().split())
friends=list(map(int,input().split()))
A=list(map(int,input().split()))
count=0
for i in range(len(A),N):
    for j in A:
        if friends[i]==j:
            count+=1
            break
print(count)
