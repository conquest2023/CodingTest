n=int(input())
data=dict()
cnt=[]
for i in range(n):
    str1,str2=input().split()
    if str2=="enter":
        data[str1]=str2
cnt2=sorted(cnt,reverse=True)
for i in cnt2:
     print(i)