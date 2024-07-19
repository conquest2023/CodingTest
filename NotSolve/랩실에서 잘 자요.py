N,M=map(int,input().split())
pages=list(map(int,input().split()))
dp=[0 for i in range(100)]
cnt=[]
result=0
last=0
for i in range(1,N+1):
    if i not in pages:
        cnt.append(i)
for i in cnt:
    if last:
        result+=min(7,(i-last)*2)
    else:
        result+=7
    last=i
print(result)