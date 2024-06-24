n=int(input())
dic=dict()
cnt=[]
for i in range(n):
    word=input()
    if word not in dic:
       dic[word]=1
    else:
        dic[word]+=1
Max=max(dic.values())

for a,b in dic.items():
    if Max<=b:
       cnt.append(a)
cnt=sorted(cnt)
print(cnt[0])
