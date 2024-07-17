import heapq
import sys
input=sys.stdin.readline
def dist(start):
    q=[]
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist2,now=heapq.heappop(q)
        if distance[now]<dist2:
            continue
        for i in graph[now]:
            cost=dist2+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

INF=int(1e9)
city=int(input())
bus=int(input())
graph=[[] for i in range(city+1)]
distance=[INF]*(city+1)
for i in range(bus):
    A,B,C=map(int,input().split())
    graph[A].append([B,C])
start,end=map(int,input().split())
dist(start)
print(distance[end])



import heapq
import sys
input=sys.stdin.readline
def dist(start):
    q=[]
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist2,now=heapq.heappop(q)
        if distance[now]<dist2:
            continue
        for i in graph[now]:
            cost=dist2+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

