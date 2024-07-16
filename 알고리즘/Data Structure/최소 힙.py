import heapq
import sys
n=int(sys.stdin.readline())
cnt = []
for i in range(n):
    m=int(sys.stdin.readline())
    if m==0:
        if len(cnt)!=0:
            print(heapq.heappop(cnt))
        else:
            print(0)
    else:
         heapq.heappush(cnt,m)


