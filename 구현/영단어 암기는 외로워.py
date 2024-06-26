n,m=map(int,input().split())
dic=dict()
cnt=[]
for i in range(n):
    word=input()
    if word not in dic and len(word)>=m:
        dic[word]=1
    else:
        if len(word)>=m:
            dic[word]+=1
###역순으로 하면 -로설정
dic=sorted(dic.items(),key=lambda x:(-x[1],-len(x[0]),x[0]))
for a in dic:
    print(a[0])

