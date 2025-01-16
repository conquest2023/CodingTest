
n=int(input())

cnt=[]
for s in range(n):
    m=list(map(int,input().split()))
    cnt.append(m)
for i in range(n):
    for j in range(n):
        for z in range(n):
            if cnt[j][i] and cnt[i][z]:
                cnt[j][z]=1

for a in range(n):
    for b in range(n):
        print(cnt[a][b],end=' ')
    print()
