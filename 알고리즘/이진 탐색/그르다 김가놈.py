N,K,M=map(int,input().split())
cnt=[]
Box=[]
for i in range(N):
    cnt.append(int(input()))
for i in cnt:
    if i<(K*2) and i-K>0:
       Box.append(i-K)
    else:
        if i - 2*K > 0:
          Box.append(i-2*K)
Box.sort()
if len(Box)==0:
    print(-1)
else:
    start = 0
    end=Box[-1]
    while start<=end and len(Box)>=1:
        mid=(start+end)//2
        total=0
        for i in Box:
            if i>0:
                total+=i//mid
        if total<M:
             end=mid-1
        else:
            start=mid+1

    print(end)
