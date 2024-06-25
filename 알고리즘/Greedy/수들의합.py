N=int(input())
Sum=N
cnt=[]
for i in range(1,N):
    Sum-=i
    if Sum<=0:
        break
    cnt.append(i)
print(cnt,Sum)
