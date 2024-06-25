def res(T2):
    if S==T2:
       print(1)
       exit(0)
    if len(T2)==0:
        return 0
    if T2[0]=="B":
       res(T2[1:][::-1])
    if T2[-1]=="A":
         res(T2[:-1])
S=list(input())
T=list(input())
res(T)
print(0)
