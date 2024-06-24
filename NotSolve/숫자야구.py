n=int(input())
cnt=[]
target=0
count=0
Str=0
for i in range(n):
    target=list(map(int,input().split()))
    cnt.append(target)
for i in range(len(cnt)-1):
    if cnt[i][1]>=cnt[i+1][1]:
        Str=cnt[i][1]
    else:
        Str=cnt[i+1][1]
target=cnt[Str]

for i in range(len(cnt)):
    if cnt[i][2]>=1 and cnt[i][1]==0:
            for j in cnt[i]:
                print(j)
                if j not in cnt[Str]:
                    count+=1
print(count)
