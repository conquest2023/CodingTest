n=int(input())
target=list(map(int,input().split()))
matter=[]
total=0
plus=0
for i in range(n):
    A,B=map(int, input().split())
    matter.append([A,B])
matter.sort()
num=0
for i in target:
    idx=0
    num+=1
    Box=[]
    for a,b in matter:
        if  a==num:
            total+=b
            Box.append(b)
            idx+=1
        if idx==i:
           if len(Box)==1 or len(Box)==0:
               break
           else:
                Min = min(Box)
                plus += b - Min
                break
print(total+plus+60*(len(target)-1))


