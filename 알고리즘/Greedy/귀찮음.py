n=int(input())

m=list(map(int,input().split()))
total=sum(m)
count=0
m.sort()
for i in m:
    total-=i
    count+=i*total
print(count)
    