n=int(input())
cnt=[0]*1001
cnt[1]=1
cnt[2]=2
cnt[3]=3
for i in range(3,n+1):
    cnt[i]=(cnt[i-1]+cnt[i-2])%10007

print(cnt[n])