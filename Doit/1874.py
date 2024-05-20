n=int(input())
cnt=[0]*n
for i in range(n):
    m=int(input())
stack=[]
num=1
result=True
answer=""
for i in range(n):
    su=cnt[i]
    if su>=num:
        while su>=num:
            stack.append(num)
            num+=1
            answer+="+\n"
        stack.pop()
        answer+="-\n"
    else:
        n=stack.pop()

        if n>su:
            print("NO")
            result=False
            break
        else:
            answer+="-\n"
if result:
    print(answer)
