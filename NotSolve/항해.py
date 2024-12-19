
N,X,Y=map(int,input().split())
idx=list(map(int,input().split()))
count=0
ans=0
idx.sort()
for i in range(len(idx)):
    if idx[i] >= X:
        if idx[i] <=Y:
            ans += 1
        else:
            if idx[i]%X<=Y-X+1:
                 ans+=idx[i]//X
            else:
                 ans+=idx[i]//Y
                 count+=idx[i]%Y
    else:
         count+=idx[i]
print(ans)
print(count)

