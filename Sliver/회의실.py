import sys
n=int(sys.stdin.readline())
cnt=[]
number=1
for i in range(n):
    a,b=list(map(int,sys.stdin.readline().split()))
    cnt.append([a,b])
print(cnt)
cnt=sorted(cnt,key=lambda x:x[1])
end=cnt[0][1]
for i in range(len(cnt)):
    if  end<=cnt[i][0]:
        end=cnt[i][1]
        number+=1
print(number)