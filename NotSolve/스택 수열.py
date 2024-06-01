Num=int(input())
count=1
answer=""
result=True
stack=[]
cnt=[]
for i in range(Num):
    m=int(input())
    stack.append(m)
for i in range(Num):
    su=stack[i]
    if su>=count:
        while su>=count:
             cnt.append(count)
             count+=1
             answer+="+\n"
        cnt.pop()
        answer+="-\n"
    else:
        n=cnt.pop()
        if n>su:
            print("NO")
            result=False
            break
        else:
            answer+="-\n"
if result:
   print(answer)