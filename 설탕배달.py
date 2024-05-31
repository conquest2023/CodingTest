import sys
target=int(sys.stdin.readline())
target2=target
n,m=3,5
count=0
if target==4:
    print(-1)
else:
    while target>=0:
        if target%m==0 :
           print(target//m)
           break
        target-=3
        count+=1

        if target<0:
            print(-1)


