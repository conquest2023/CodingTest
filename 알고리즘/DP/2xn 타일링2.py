n=int(input())
Box=[0]*1001
Box[0]=1
Box[1]=1
for i in range(2,n+1):
    Box[i]=Box[i-1]+2*Box[i-2]
print(Box[n]%10007)