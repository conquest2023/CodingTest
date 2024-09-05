n=int(input())
word=[]
for i in range(n):
    words=input().split(".")
    word.append(words[1])

word.sort()
dic=dict()

for i in word:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1

for a,b in dic.items():
    print(a,b)