n,m=list(map(int,input().split()))

data=dict()
data2=dict()
sum=0
for i in range(n):
    a=input()
    data[a]=0
for i in range(m):
    b=input()
    data2[b]=0
for i in data2.keys():
    if i in data.keys():
       sum+=1
print(sum)               