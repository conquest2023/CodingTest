N,A,B=map(int,input().split())
cnt=[]
total=0
for i in range(N):
    a,b=list(map(int,input().split()))
    cnt.append([a,b,abs(a-b)])
cnt=sorted(cnt,key=lambda x:-x[2])
for i in range(N):
    if cnt[i][0]<cnt[i][1] and A!=0 or B<=0:
        total+= cnt[i][0]
        A-=1
    else:
        total += cnt[i][1]
        B-=1
print(total)
