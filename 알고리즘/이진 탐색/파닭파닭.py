N,M=map(int,input().split())
cnt=[]
for i in range(N):
    cnt.append(int(input()))

start=1
end=cnt[-1]

while start<=end:
     mid = (start + end) // 2
     count=0
     for i in cnt:
         count+=i//mid
     if M<=count:
         start=mid+1
     else:
         end=mid-1
print(sum(cnt)-(M*end))

"""망한 코드
def search(idx):
    global count,total
    start=0
    end=len(cnt)-1
    while start<=end:
        if  cnt[start]-idx>=idx:
            count+=(cnt[start])//idx
            total+=(cnt[start])%idx
        else:
            total += cnt[start]-idx
            count+=1
        start += 1
    return count
N,M=map(int,input().split())
cnt=[]
for i in range(N):
    cnt.append(int(input()))
start=0
count=0
end=len(cnt)-1
total=0
cnt.sort()
idx=cnt[0]
for i in range(cnt[0],-1,-1):
    search(idx)
    if count==5:
       print(total)
       break
    count=0
    idx -= 1
    total=0



"""