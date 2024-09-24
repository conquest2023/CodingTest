def recursion(X,Y,N):
    color=cnt[X][Y]
    for i in range(X,X+N):
        for j in range(Y,Y+N):
            if color != cnt[i][j]:
                recursion(X,Y,N//2)
                recursion(X,Y+N//2,N//2)
                recursion(X+N//2,Y,N//2)
                recursion(X+N//2,Y+N//2,N//2)
                return
    if color==0:
        result.append(0)
    else:
        result.append(1)




N=int(input())
cnt=[]
result=[]
for i in range(N):
    cnt.append(list(map(int,input().split())))

recursion(0,0,N)
print(result.count(0))
print(result.count(1))