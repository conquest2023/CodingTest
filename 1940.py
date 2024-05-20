n=int(input())
m=list(map(int,input().split()))
start=0
end=1
count=0
m.sort()
for i in range(n):
    find=m[i]
    a=0
    b=n-1
    while a<b:
        if m[a]+m[b]==find:
            if a!=i and b!=i:
               count+=1
               break
            elif a==i:
                a+=1
            elif b==i:
                 b-=1
        elif m[a]+m[b]< find:
             a+=1
        else:
             b-=1
print(count)

