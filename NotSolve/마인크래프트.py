"""
a,b,c=list(map(int,input().split()))
arr=[]
num=0
for i in range(a):
   arr.append(list(map(int,input().split())))
   number=max(arr[i])
for i in range(a):
   for j in range(b):
         if arr[i][j]==number and arr[i-1][j-1]<number:
            if c>0:
               num+=2
               arr[i][j]-=1
         if c==0 and arr[i][j]>number:
            num +=2
            arr[i][j]-=1
         if arr[i][j]!=number and arr[i-1][j-1]<number and c>0:
               num+=1
               arr[i][j]+=1

print(num ,arr[0][0]"""




N,M,B=map(int,input().split())
cnt=[]
for i in range(N):
    ground=list(map(int,input().split()))
    cnt.append(ground)
time=0
Box=[]
for i in range(N):
    for j in range(M):
        if cnt[i][j]:

