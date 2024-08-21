N,M=map(int,input().split())
cnt=[]
for i in range(N):
    cnt.append(int(input()))
cnt.sort()
start=1
end=cnt[-1]

while start<=end:
    total = 0
    mid = (start + end) // 2
    for i in cnt:
        total+=i//mid
    if  M<=total:
        start=mid+1
    else:
        end=mid-1
print(end)
