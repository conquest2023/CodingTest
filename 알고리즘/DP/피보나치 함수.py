N=int(input())
d=[0]*(N+1)
d[1]=1
d[2]=1
num=40
for i in range(3,num+1):
    d[i]=d[i-1]+d[i-2]
for i in range(N):
    m=int(input())
    if m==0:
      print(0,1)
    elif m==1:
        print(1,0)
    else:
        print(d[m-1],d[m])


"""def fib(N):
    zeros = [1, 0, 1]
    ones = [0, 1, 1]
    if N >= 3:
        for i in range(2, N):
            zeros.append(zeros[i - 1] + zeros[i])
            ones.append(ones[i - 1] + ones[i])
    print(f"{zeros[N]} {ones[N]}")


T = int(input())
for _ in range(T):
    N = int(input())
    fib(N)"""