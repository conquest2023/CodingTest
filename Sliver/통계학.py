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
    count=1
    if i in pocket.keys():
        count+=1
        pocket[i] = count
    else:
        pocket[i]=1
Max=max(pocket.values())
print(pocket)
if len(cnt)==1:
    print(cnt[0])
elif len(cnt)!=1 and Max==1:
    print(cnt[1])
else:
    print()


