n=list(input())
cnt=[]
a=""
num=0
for i in range(len(n)):
    if n[i]>='0':
       a=a+n[i]
    elif n[i]=="+" or n[i]=="-":   
       cnt.append(a)       
if "+" in n and "-" in n:
    print(n)
else:
     print(1)