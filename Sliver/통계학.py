import sys
n=int(sys.stdin.readline())
cnt=[]
cnt2=[]
pocket=dict()
pocket2=dict()
for i in range(n):
    m=int(sys.stdin.readline())
    cnt.append(m)
cnt.sort()
print(round(sum(cnt)/(len(cnt))))
if len(cnt)==1:
    print(cnt[0])
else:    
    print(cnt[int(len(cnt)//2)])
for i in cnt:
    if i in pocket.keys():
        pocket[i]+=1
    else:
        pocket[i]=1
Max=max(pocket.values())
for a,b in pocket.items():
    if b==Max:
       cnt2.append(a)
cnt2.sort()
if len(cnt2)>1:
    print(cnt2[1])
else:
    print(cnt2[0])
if len(cnt)==1:
    print(0)
else:
    print(max(cnt)-(min(cnt)))