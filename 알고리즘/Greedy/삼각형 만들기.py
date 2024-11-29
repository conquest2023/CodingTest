n=int(input())
cnt=[]
for i in range(n):
    m=int(input())
    cnt.append(m)
cnt.sort(reverse=True)
ans=[]
for i in range(2,n):
    if cnt[i-2]<cnt[i]+cnt[i-1]:
        ans.append( cnt[i-2]+cnt[i]+cnt[i-1])

if len(ans)==0:
    print(-1)
else:
    print(max(ans))