a,b,c=map(int,input().split())
cnt=list(map(int,input().split()))
cnt.sort()
result=0
frist=cnt[a-1]
second=cnt[a-2]
while True:
    for i in range(c):
        if b==0:
            break
        result+=frist
        b-=1
    if b==0:
        break
    result+=second
    b-=1
print(result)
