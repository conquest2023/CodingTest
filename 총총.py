n=int(input())
num=0
cnt=set()
for i in range(n):
    a,b=input().split()
    cnt.add(a)
    cnt.add(b)
    if a=="ChongChong" or b=="ChongChong":
        num+=1
        cnt.clear()    
print(cnt)

 