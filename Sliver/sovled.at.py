def flo(n):

    if n-int(n)>=0.5:
        return (int(n)+1)
    else:
         return int(n)
n=int(input())
cnt=[]
if n:
    for i in range(n):
        m=int(input())
        cnt.append(m)
    miduem=flo(n*0.15)

    cnt=sorted(cnt)
    for i in range(miduem):
        cnt.pop()
        cnt.pop(0)
    print((flo(sum(cnt)/len(cnt))))
else:
     print(0)


