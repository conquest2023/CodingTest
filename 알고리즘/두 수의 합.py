num=int(input())
collect=list(map(int,input().split()))
collect.sort()
cnt=[]
left,right=0,len(collect)-1
while not left==right:
    if collect[left]+collect[right]<0:
            cnt.append([collect[left],collect[right]])
            left+=1
    elif collect[left]+collect[right]>0:
            cnt.append([collect[left], collect[right]])
            right-=1
    else:
         cnt.append([collect[left], collect[right]])
         right-=1

target=0
for a,b in cnt:
    if a+b<target:
       target=a+b

print(target)

