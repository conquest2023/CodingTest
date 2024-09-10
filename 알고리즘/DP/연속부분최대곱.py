def Round(num):
    num

N=int(input())
cnt=[]
Max=0

for i in range(N):
    cnt.append(float(input()))

for i in range(N):
    Sum=cnt[i]
    for j in range(i+1,N):
        Max=max(Sum,Max)
        Sum *= cnt[j]
print('%0.3f' % Max)

