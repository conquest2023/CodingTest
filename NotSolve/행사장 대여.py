# N=int(input())
# Box=[]
# for i in range(N):
#     M=list(map(int,input().split()))
#     Box.append(M)
# Max=[]
# Max_x = 0
# Max_y = 0
# for x1,y1,x2,y2 in Box:
#     if Max_x <=x2:
#         Max_x=x2
#     if Max_y <= y2:
#         Max_y=y2
#     Max.append(Max_x* Max_y)
#
# print(max(Max))
import sys
input = sys.stdin.readline

N = int(input())


board = [[0 for _ in range(500)] for _ in range(500)]
res = 0
ans=0
for i in range(N):
    x1,y1,x2,y2 = map(int,input().split())
    for j in range(y1,y2):
        for k in range(x1,x2):
            board[j][k]+=1


for row in range(500):
    for col in range(500):
        if board[row][col] > 0:
            res+=1
print(res)