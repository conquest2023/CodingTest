def Num(num):
   start=0
   end=num
   middle=end//2
   while start<=end:
        if



N,K,M=map(int,input().split())
cnt=[]
cnt2=[]
count=[]
for i in range(N):
    cnt.append(int(input()))
for i in cnt:
    if i-K*2>0:
       cnt2.append(i-K*2)
    elif i-K*2<0 and i-K>0:
        cnt2.append(i-K)
##큰값으로 하면 작은값을 나눌수있다
Num(max(cnt2))


