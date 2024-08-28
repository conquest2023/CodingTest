N,M,K=map(int,input().split())
Box=[]
ans=0
for i in range(K):
    word=list(map(int,input().split()))

    Box.append(word)
#cnt=sorted(cnt,key=lambda x:x[1])
Box.sort(reverse=True)
start=0
end=2**31
while start<=end:
    count=0
    mid=(start+end)//2
    total= 0
    for a,b in Box:
        if mid>=b:
            total+=a
            count+=1
        if count==N:
            break
    if total>=M and count==N:
         end=mid-1
    else:
        start=mid+1
if end!=2**31:
    print(start)
else:
    print(-1)
