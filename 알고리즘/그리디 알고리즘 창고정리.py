n=int(input())
m=list(map(int,input().split()))
count=int(input())
m.sort()
cnt=[]

print(m)
for i in range(count):
    m[n-1]-=1
    m[0]+=1
    m.sort()
print(max(m)-min(m))
