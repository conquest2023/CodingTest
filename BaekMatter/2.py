n=int(input())
cnt=[]
cnt2=[]
count=0
for i in range(n):
    cnt.append(list(input()))
for i in cnt:
    cnt3=sorted(i)
    cnt2.append(cnt3)
for i in range(len(cnt)):
    if len(set(cnt[i]))==1 or len(cnt[i])==2:
        count+=1
    elif cnt[i]==cnt2[i]:
         count+=1

print(count)




