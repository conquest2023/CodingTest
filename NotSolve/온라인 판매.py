"""N,M=map(int,input().split())
cnt=[]
total=[]
idx=[]
idx2=[]
for i in range(M):
    cnt.append(int(input()))
cnt.sort()
j=M
for i in range(M):
    idx.append([cnt[i],cnt[i]*j])
    idx2.append(cnt[i]*j)
    j-=1
Max=max(idx2)

for a,b in idx:
    if b>=Max:
       total.append([a,b])
total=sorted(total,key=lambda x:(x[0]))
print(total[0][0],total[0][1],end=' ')

"""

n, m = map(int, input().split())

p = []
for _ in range(m):
    p.append(int(input()))

p.sort()  # 오름차순으로 정렬

result = 0  # 총 수익
A = 0  # 달걀 가격
for i in range(m):
    # i번째 가격을 채택하면 p[i]보다 싼 가격을 원하는 고객은 구매하지 않으므로 구매할 고객의 수를 구한다.
    cnt = m - i

    if n <= cnt:  # 달걀의 수가 고객보다 적다면 모든 달걀을 다 팔아야 함
        sum = n * p[i]
    else:
        sum = cnt * p[i]

    if sum > result:
        result = sum
        A = p[i]

print("%d %d" % (A, result))