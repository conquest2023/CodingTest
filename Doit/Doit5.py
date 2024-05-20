n,m=map(int,input().split())
n=list(map(int,str(n)))
cnt=[]
for i in n:
    while cnt and  m>0 and cnt[-1]<i:
        cnt.pop()
        m-=1
    cnt.append(i)
if m!=0:
   cnt=cnt[:-m]

res=''.join(map(str,cnt))
print(res)
