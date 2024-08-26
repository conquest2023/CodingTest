N,M=map(int,input().split())
Box=list(map(int,input().split()))

Box.sort()

start=0
end=Box[-1]
while start<=end:
    total=0
    mid=(start+end)//2
    for i in Box:
        if i-mid>0:
           total+=i-mid
    if total>=M:
        start=mid+1
    else:
        end=mid-1
print(end)