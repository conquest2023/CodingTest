"""N=int(input())
for i in range(N):
    A=int(input())
    count=0
    num=0
    total=[]
    Max=0
    M=list(map(int,input().split()))
    reverse_M=sorted(M,reverse=True)
    Max_price=reverse_M[0]
    for i in M:
        total.append(i)
        Max=max(i,Max)
        if Max==Max_price and len(total)>1:
            for i in total:
                count += Max - i
            total=[]
            Max=0
            num+=1
            Max_price = reverse_M[num]
    if len(total)>=2:
        Max2=max(total)
        for i in total:
            count+=Max2-i
    print(count)

"""
T = int(input())
for _ in range(T):
    N = int(input())
    stock = list(map(int, input().split()))
    stock.reverse()
    max = stock[0]
    sum = 0

    for i in range(1, N):
        if max < stock[i]:
            max = stock[i]
            continue
        sum += max - stock[i]

    print(sum)