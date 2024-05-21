n,m=map(int,input().split())
cnt=dict()
cnt2=[]
for i in range(n):
    word=input()
    if len(word)<m:
       continue
    else:
        if word in cnt:
            cnt[word]+=1
        else:
            cnt[word]=1
for a,b in cnt.items():
    cnt2.append([a])
    cnt2.append([b])
print(cnt2)
cnt2=sorted(cnt2[1],reverse=True)
print(cnt2)