import sys
n,m,k=map(int,sys.stdin.readline().split())
Sum1=0
Sum2=0
menu=dict()
menu2=dict()
menu3=[]
PlusMenu=0
SpecialMenu=0
for i in range(n):
    order,count=sys.stdin.readline().split()
    menu[order]=int(count)
for i in range(m):
    order2,count2=sys.stdin.readline().split()
    menu2[order2]=int(count2)
for i in range(k):
    order3=input()
    menu3.append(order3)
plus=int(input())
for i in range(plus):
    last=input()
    if last in menu:
        Sum1+=menu[last]
    elif last in menu2:
        Sum2+=menu2[last]
        SpecialMenu +=1
    elif last in menu3:
         PlusMenu+=1
total=Sum1+Sum2
res="Okay"
if Sum1<20000 and SpecialMenu>0:
    res="No"
else:
    if total<50000 and SpecialMenu>0:
        res = "No"
    elif PlusMenu> 1:
        res = "No"

print(res)

"""
import sys

A, B, C = map(int, sys.stdin.readline().split())

dt_A = dict()
dt_B = dict()
li_C = list()

for i in range(A):
    menu = sys.stdin.readline().split()
    dt_A[menu[0]] = int(menu[1])

for i in range(B):
    menu = sys.stdin.readline().split()
    dt_B[menu[0]] = int(menu[1])

for i in range(C):
    li_C.append(sys.stdin.readline().rstrip())

N = int(sys.stdin.readline())
A_price = 0
B_price = 0
B_cnt = 0
C_cnt = 0
for i in range(N):
    menu = sys.stdin.readline().rstrip()
    if menu in dt_A.keys():
        A_price += dt_A[menu]
    elif menu in dt_B.keys():
        B_price += dt_B[menu]
        B_cnt += 1
    else:
        C_cnt += 1

res = "Okay"
if A_price < 20000 and B_cnt > 0:
    res = "No"
else:
    if A_price + B_price < 50000 and C_cnt > 0:
        res = "No"
    elif C_cnt > 1:
        res = "No"

print(res)
"""
