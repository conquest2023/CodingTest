N,M=map(int,input().split())
cnt=[]
Max=0
for i in range(N+M):
    X,Y=map(int,input().split())
    cnt.append([X,Y])
    if Max<Y:
        Max=Y
print(Max)
