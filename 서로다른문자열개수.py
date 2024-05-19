n=(input())
m=set()
for i in range(len(n)):
    for j in range(i,len(n)):
        m.add(n[i:j+i])
print(m)