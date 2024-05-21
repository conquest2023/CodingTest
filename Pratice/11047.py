n,m=list(map(int,input().split()))
cnt=[]
k=0
for i in range(n):
    b=int(input())
    cnt.append(b)
d=reversed(cnt)    

while 1:
     if m==0:
        break
     for i in d:
        if m//i==0:
           pass
        elif m%i>=0:   
           k+=(m//i)
           m=(m%i)
print(k)            




    
 