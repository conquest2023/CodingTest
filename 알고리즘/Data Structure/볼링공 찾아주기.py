import sys
N=int(sys.stdin.readline())
dic=dict()
for i in range(N):
    idx=list(map(int,sys.stdin.readline().split()))
    if  idx[0]==1:
        dic[idx[2]]=idx[1]
    else:
         print(dic[idx[1]])





