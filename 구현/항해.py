
N,X,Y=map(int,input().split())
idx=list(map(int,input().split()))
count=0
ans=0
for i in range(len(idx)):
    if idx[i] >= X:
        if idx[i] <Y:
            ans += 1
        else:
             A=idx[i]//X
             B=idx[i]//Y
             if A>B:
                ans+=A
             else:
                  ans+=B
                  count+=idx[i]%Y
    else:
         count+=idx[i]
print(ans)
print(count)

