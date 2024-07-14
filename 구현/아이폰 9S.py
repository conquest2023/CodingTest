N=int(input())
cnt=[]

for i in range(N):
    cnt.append(int(input()))


Max_count=0
idx=set(cnt)

for i in idx:
    ans = 1
    cut=[j for j in cnt if i!= j]

    for z in range(len(cut)-1):
        if cut[z]==cut[z+1]:
            ans+=1
        else:
            Max_count=max(Max_count,ans)
            ans=1
    Max_count=max(Max_count,ans)

print(Max_count)

