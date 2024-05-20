import sys
n=int(sys.stdin.readline())
m=list(map(int,sys.stdin.readline().split()))
arr={m[i]:i for i in range(len(m))}
num=0
cnt=[]
for i in m:
    num=0
    for a,b in arr.items():
        if i>a:
           num+=1
    cnt.append(num)
for i in cnt:
    print(i,end=' ')
#시간초과
