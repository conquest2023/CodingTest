num=int(input())
collect=list(map(int,input().split()))
collect.sort()
target=int(input())
count=0
left,right=0,len(collect)-1
while not left==right:
    if collect[left]+collect[right]<target:
            left+=1
    elif collect[left]+collect[right]>target:
            right-=1
    else:
         count+=1
         right-=1
print(count)