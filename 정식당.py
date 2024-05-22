n,m,k=map(int,input().split())
Sum=[]
menu=dict()
menu2=[]
menu3=[]
for i in range(n):
    order,count=input().split()
    count=int(count)
    menu[order]=count
for i in range(m):
    order2=input()
    menu2.append(order2)
for i in range(k):
    order3=input()
    menu3.append(order3)
plus=int(input())
for i in range(plus):
    last=input()
    if last in menu.keys():

print(Sum)