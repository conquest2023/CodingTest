n=int(input())
cnt=[0]*91
cnt[1]=1
cnt[2]=1
if n==3:
    print(2)
else:
    for i in range(3,n+1):
        cnt[i]=cnt[i-2]+cnt[i-1]
    print(cnt[n])