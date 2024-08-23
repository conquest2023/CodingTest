N=int(input())
M=list(map(int,input().split()))
cnt=list(input())
total=[0]*len(cnt)
for i in range(len(cnt)):
    if cnt[i]=="B":
       total.append(M[0]-total[-1]-1)
    if cnt[i]=="S":
        total.append(M[1]-total[-1]-1)
    if cnt[i]=="G":
        total.append(M[2] - total[-1]-1)
    if cnt[i]=="P":
        total.append(M[3] - total[-1]-1)
    if cnt[i]=="D":
         total.append(M[3])
print(sum(total))