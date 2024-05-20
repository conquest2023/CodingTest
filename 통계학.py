n=int(input())
cnt=[]
pocket=dict()
for i in range(n):
    m=int(input())
    cnt.append(m)
cnt.sort()
print(round(sum(cnt)/(len(cnt))))
if len(cnt)==1:
    print(cnt[0])
else:    
    print(cnt[int(len(cnt)//2)])

for i in cnt:
    if i in pocket:
        pocket[i]+=1
    else:
        pocket[i]=1 
mx=max(pocket.values())
cnt2=[]
for i in pocket:
    if mx==pocket[i]:
        cnt2.append(i)
if len(cnt2)>1:
    print(cnt2[1])
else:
    print(cnt2[0])           

print(max(cnt)-min(cnt))


    