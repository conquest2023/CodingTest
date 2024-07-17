import heapq
import sys
INF=int(1e9)
input=sys.stdin.readline
def dijkstra(num):
    q=[]
    heapq.heappush(q,(0,num))
    distance[num]=0
    while q:
         dist, now = heapq.heappop(q)
         if  distance[now]<dist:
                continue
         for i in graph[now]:
             cost=dist+i[1]
             if cost<distance[i[0]]:
                 distance[i[0]]=cost
                 heapq.heappush(q,(cost,i[0]))

n = int(input())
for i in range(n):
    V,E=map(int,input().split())
    total=[0]*(V+1)
    graph = [[] for i in range(V + 1)]
    for i in range(E):
        A,B,C=map(int,input().split())
        graph[A].append([B,C])
        graph[B].append([A,C])
    number=int(input())
    friends=list(map(int,input().split()))
    for i in friends:
        distance = [INF] * (V + 1)
        dijkstra(i)
        for j in range(1,V+1):
            total[j]+=distance[j]
    min = 0
    now = INF
    for i in range(1,V+1):
        if now>total[i]:
            now=total[i]
            min=i
    print(min)
"""
import sys                        
input = sys.stdin.readline  
INF = 100001

if __name__ == '__main__':
  for _ in range(int(input())):
    # Input
    N, M = map(int, input().split())   

    dists = [[INF]*(N+1) for _ in range(N+1)]
    for _ in range(M):
      a, b, c = map(int, input().split())
      dists[a][b] = c
      dists[b][a] = c 

    int(input()) # K
    rooms = list(map(int, input().split()))


    # Floyd-Warshall
    for k in range(1, N+1):
      dists[k][k] = 0
      for i in range(1, N+1):
        for j in range(1, N+1):
          dists[i][j] = min(dists[i][j], dists[i][k] + dists[k][j])


    # Print minDistNode
    minDistSum = float('inf')
    minDistNode = 0

    for i in range(1, N+1):
      distSum = sum(dists[room][i] for room in rooms)
      if minDistSum > distSum:
        minDistSum = distSum
        minDistNode = i

    print(minDistNode)
"""