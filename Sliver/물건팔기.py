N=int(input())
cnt=[]
Max=0
ans=[]
for i in range(N):
    cnt.append(list(map(int,input().split())))
cnt=sorted(cnt,key=lambda x:x[0])
for i in range(N):
    total=0
    for j in range(i,N):
        if cnt[i][0]-cnt[j][1]>0:
            total+=cnt[i][0]-cnt[j][1]
    if Max<total:
       Max=max(total,Max)
       ans.append(cnt[i])
if Max<=0:
    print(0)
else:
    print(ans[-1][0])

