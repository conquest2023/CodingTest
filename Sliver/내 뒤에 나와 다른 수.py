# import sys
# n=int(sys.stdin.readline())
# M=list(map(int,sys.stdin.readline().split()))
# ans=[]
# count=0
# for i in M:
#     count+=1
#     for j in  range(count,n):
#
#         if  i!=M[j%n]:
#             ans.append(j+1)
#             break
#         if j >= n - 1:
#             ans.append(-1)
#             break
# ans.append(-1)
# for i in ans:
#     print(i,end=' ')
import sys
n = int(sys.stdin.readline())
M=list(map(int,sys.stdin.readline().split()))
count=0
ans=[]
for i in range(n):
    if i==0:
        count+=1
    elif M[i]==M[i-1]:
        count+=1
    else:
        for _ in range(count):
            print(i+1,end=' ')
        count=1
for _ in range(count):
    print(-1, end=' ')