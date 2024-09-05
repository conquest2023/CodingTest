n=input()
cnt=[]

for i in range(len(n)):
    word = ""
    for j in range(i,len(n)):
        word+=n[j]
    cnt.append(word)
cnt=sorted(cnt,key=lambda x:(x[0:]))
for i in cnt:
    print(i)