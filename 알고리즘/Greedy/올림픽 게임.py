import sys

N=int(sys.stdin.readline())
for i in range(N):
    cnt = []
    day=0
    M = int(sys.stdin.readline())
    ans=0
    time=0
    for j in range(M):
        d,s,e=map(int,sys.stdin.readline().split())
        cnt.append([d,s,e])
    cnt=sorted(cnt,key=lambda x:(x[0],x[2]))
    for A in range(len(cnt)):
        if cnt[A][0]>day:
            day=cnt[A][0]
            time=cnt[A][2]
            ans+=1
        else:
            if cnt[A][1]>=time:
                time=cnt[A][2]
                ans+=1
    print('Scenario #{}:'.format(i + 1))
    print(ans)
    print()

        # if idx!=cnt[A][0]:
        #     ans+=1
        #     idx=cnt[A][0]
        # time=cnt[A][2]
        # for B in range(A,len(cnt)-1):
        #     if cnt[A][0]==cnt[B][0]:
        #          if time<cnt[B+1][1]:
        #              time=cnt[B+1][2]
        #              ans+=1

