n=int(input())
cnt=[]
count=0
for i in range(n): 
    m=list(map(int,input().split()))
    cnt.append(m)

cnt=sorted(cnt,key=lambda x:(x[1]))
print(cnt)
data=cnt[0]
for a,b in cnt:
    if a<b:
        count+=1
        data[0][1]=cnt[i][0]
print(data)        


