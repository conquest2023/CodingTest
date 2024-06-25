"""
n=int(input())
cnt=[]
rank=n
for i in range(n):
    a,b=map(int,input().split())
    cnt.append((a,b))
for a,b in cnt:
    while True:
        for c,d in cnt:
            if a <c and b<d:
                rank-=1
                print(a,b)
        break
"""
""" 개선된 코드"""
n=int(input())
body=[]
rank=n
for i in range(n):
    a,b=map(int,input().split())
    body.append((a,b))
body.sort(reverse=True)
largest=0
cnt=0
for a,b in body:
    if b>largest:
        largest=b
        cnt+=1
print(cnt)

