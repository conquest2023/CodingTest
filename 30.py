"""from collections import deque
n=list(input())
word=""
if "0" in n:
   zero=n.remove("0")
   n.append(zero)
queue=deque(n)
for i in n:
    word+=i
word=int(word)
cnt2=[]
if word%30==0:
   print(word)
elif "0" not in n:
    print(-1)
else:
    while True:
        for i in n:
            word2 = ""
            a = queue.po()
            queue.append(a)
            for j in queue:
                word2 += j
                if int(word2) % 30 == 0 and int(word2) > 0:
                    cnt2.append(word2)
"""

N = list(input())
N = sorted(N, reverse=True)

if N[-1] != '0' :
    print(-1)
else:
    sum = 0
    for i in N:
        sum += int(i)
    if sum % 3 != 0 :
        print(-1)
    else :
        print(''.join(N))