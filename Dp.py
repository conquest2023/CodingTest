num=int(input())
count=0

for i in range(num):
    num-=1
    count+=1
    if num == 1:
        break
    if num%5==0:
       num=num//5
       count+=1
    elif num!=0 and num%3==0:
        num=num//3
        count+=1
    elif num%2==0 and num!=0:
       num=num//2
       count+=1
print(count)