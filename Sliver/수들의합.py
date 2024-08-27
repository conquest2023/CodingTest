N=int(input())
total=0
count=0
for i in range(1,N+1):
    total+=i
    count+=1
    if total>=N:
        break
if total==N:
    print(count)
else:
    print(count-1)