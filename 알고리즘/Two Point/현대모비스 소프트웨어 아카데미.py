# from collections import deque
# import sys
# N,M=map(int,sys.stdin.readline().split())
# idx=list(map(int,sys.stdin.readline().split()))
# count = 0
# cnt=0
# for i in range(N-1):
#     if idx[i]+idx[i+1]>=10 and i not in cnt:
#         cnt+=i+1
#         count+=1
# print(count)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
point = list(map(int, input().split()))
point.sort()

start = 0
end = N - 1

result = 0
while start < end:
    K = point[start] + point[end]
    if K >= M:
        result += 1
        start += 1
        end -= 1
    else:
        start += 1

print(result)