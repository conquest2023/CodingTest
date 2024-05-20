n=int(input())
num1=list(map(int,input().split()))
m=int(input())
num2=list(map(int,input().split()))

start=0
end=max(num1)

cnt=[]
def count(array,target,start,end):
    while(start<=end):
        mid=(start+end)//2
        if array[mid]==target:
            return mid 
        if target<mid:
            end=mid-1
        else:
            start=mid+1
    return None
for i in range(n):
    result=count(num1,num2[i],0,n-1)
    if result==None:
        cnt.append(0)
    else:
        cnt.append(1)

for i in cnt:
    print(i)

