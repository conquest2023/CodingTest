n=int(input())
target=int(input())
menu=list(map(int,input().split()))
menu.sort()
left=0
count=0
right=n-1
while left<right:
     if menu[left]+menu[right]<target:
         left+=1
     elif menu[left]+menu[right]>target:
         right-=1
     else:
         count+=1
         left+=1
         right-=1
print(count)
