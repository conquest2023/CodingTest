
def Count(len):
    cnt2=0
    for x in cnt:
        cnt2+=(x//len)
    return cnt2
n,m=map(int,input().split())
cnt=[]
res=0
largest=0

for i in range(n):
    a=int(input())
    cnt.append(a)
lt=1
rt=max(cnt)
while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid)>=m:
        res=mid
        lt=mid+1
    else:
        rt=mid-1
print(res)


