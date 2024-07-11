n,m=map(int,input().split())
cnt=[]
X=0
Y=0
for i in range(n):
    A,B=map(int,input().split())
    cnt.append([A,B])
    X+=A
    Y+=B
X=X//n
Y=Y//n
cnt.sort()
print(cnt)

"""if len(cnt)<=2:
    if len(cnt)==1:
        print(cnt[0][0]+cnt[0][1])
    else:
        cnt.sort()
        print(cnt[1][0]-cnt[0][0]+cnt[1][1]-cnt[0][1])
if len(cnt)>2 and 
"""