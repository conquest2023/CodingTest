
n,m=input().split()
n=int(n)
m=int(m)
cnt2=[]
for i in range(n):
    cnt=int(input())
    cnt2.append(cnt)
cnt2.sort()
up=0
end=max(cnt2)
result=0
while up<=end:
    total=0
    mid=(up+end)//2
    for x in cnt2:
        if x>mid:
           total+=x//mid
    if total<m:
        end=mid-1
    else:
        result=mid
        up=mid+1

print(result)
