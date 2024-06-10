n=int(input())

count=0
if n==2:
    print(1)
else:
    while n>=0:
        if n%5==0:
            print(n//5+count)
            break
        if n==0:
           break
        n-=2
        count+=1
        if n<=-1:
            print(-1)
            break

