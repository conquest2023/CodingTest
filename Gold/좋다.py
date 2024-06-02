n=int(input())
number=list(map(int,input().split()))
number.sort()
count=0
for i in range(len(number)):
    find=number[i]
    first=0
    end =n-1
    while first<end:
        if number[first]+number[end]==find:
           if first!=i and end!=i:
              count+=1
              break
           elif first==i:
                first+=1
           elif end==i:
                end-=1
        elif number[first]+number[end]<find:
             first+=1
        else:
             end-=1
print(count)