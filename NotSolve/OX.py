# N=list(input())
# count=0
# n=0
# if len(N)==1:
#     print(0)
# else:
#     while True:
#         idx=0
#         count+=1
#         # n=idx%(len(N))
#         if N.count("X")==len(N):
#             break
#         for i in range(len(N)):
#             idx+=1
#             if "O"==N[i]:
#                 N[0]="X"
#                 for i in range(idx-1):
#                     if "X"==N[i]:
#                         N[i]="O"
#                 N[idx-1]="X"
#                 break
# print(count)
#
#
import sys

input = sys.stdin.readline

S = list(input().rstrip())
R = 10 ** 9 + 7
data = [1] * len(S)
for i in range(1, len(S)):
    data[i] = (data[i - 1] * 2) % R
ans = 0
for i in range(len(S)):
    if S[i] == 'O':
        ans = (ans + data[i]) % R
print(ans)