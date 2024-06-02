import sys
import heapq
n=int(sys.stdin.readline())
cnt=[]
for i in range(n):
    target=int(sys.stdin.readline())
    heapq.heappush(cnt,-target)
    if target==0:
       print(-heapq.heappop(cnt))
