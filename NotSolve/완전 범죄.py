import sys
from collections import deque

INF=2e9
def bfs(start,goal):
    queue=deque()
    visit=[0]*(N+1)
    queue.append([start,0])
    visit[start]=1
    for office in I:
        visit[office]=1
    while queue:
        here,click=queue.popleft()
        if here==goal:
            return click
        for a in [here+F,here-B]:
            if 1<=a <=N and not visit[a]:
                visit[a]=1
                queue.append([a,click+1])
    return INF
def S():
    press_count=bfs(S,D)
    return  press_count if press_count!= 0 else 'BUG FOUND'
if __name__=='__main__':
    N,S,D,F,B,K=list(map(int,input().split()))
    I=list(map(int,input().split()))
    answer=S()
    print(answer)