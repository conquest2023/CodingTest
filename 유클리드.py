def gcb(a,b):
    while a!=0:
       a,b=b%a,a
    return b



a,b=input().split()
c,d=input().split();

a=int(a)
b=int(b)
c=int(c)
d=int(d)
num1=a*d+b*c
num2=b*d
print(int(num1/gcb(num1,num2)),int(num2/gcb(num1,num2)))