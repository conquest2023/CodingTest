N=int(input())
words=list(map(int,input().split()))
M=int(input())
words.sort()
start=0
end=words[-1]
while start<=end:
    mid=(start+end)//2
    total = 0
    target = M
    for i in words:
        if i-mid<=0:
           total+=i
        else:
            total+=mid
    if total<=target:
        start=mid+1
    else:
        end=mid-1
print(end)