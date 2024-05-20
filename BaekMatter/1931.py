n=int(input())
cnt=[]
count=0
for i in range(n): 
    a,b=(map(int,input().split()))
    cnt.append((a,b))
cnt.sort(key=lambda x: (x[1], x[0]))

time=0
answer=0
for a in cnt:
    if time <=a[0]:
        time =a[1]
        count+=1
print(count)        
       