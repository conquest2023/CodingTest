

n=int(input())

dp=[0]*(n+1)
dp[1]=1
count=0
for i in range(2,len(dp)):
    dp[i]=i*i
for i in range(len(dp)-1,0,-1):
    if n == 0 or n<0:
        break
    if  dp[i]<=n:
        print(dp[i])
        n=n-dp[i]
        count+=1
if n!=0:
   print(count+n)
else:
    print(count)