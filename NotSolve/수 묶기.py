
n=int(input())

cnt=[]
ans=[]

plusCount=0
minusCount=0
for i in range(n):
    m=int(input())
    if m<=0:
        ans.append(m)
    else:
        cnt.append(m)
cnt.sort(reverse=True)
ans.sort()
for i in range(1,len(ans),2):
     if ans[i - 1] + ans[i] < ans[i - 1] * ans[i]:
         minusCount += ans[i - 1]* ans[i]
     else:
         minusCount += ans[i - 1]+ans[i]
if len(ans)%2!=0:
    minusCount+=ans[-1]
for i in range(1,len(cnt),2):
    if cnt[i-1]+cnt[i] < cnt[i-1]*cnt[i]:
        plusCount+=cnt[i-1]*cnt[i]
    else:
         plusCount+=cnt[i-1]+cnt[i]
if len(cnt)%2!=0:
    plusCount+=cnt[-1]
print(minusCount+plusCount)

