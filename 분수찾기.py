n=5
cnt=[]
length=[]
for i in range(n):
    word=input()
    cnt.append(word)
    length.append(len(word))
print(length)
for i in range(max(length)):
    for j in range(5):
        if  i<length[j]:
            print(cnt[j][i],end='')

