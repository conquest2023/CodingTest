from collections import deque

n,m=map(int,input().split())
cnt=list(map(int,input().split()))
queue=deque(cnt)
count=0
target=queue[m]
while True:

    largest=max(queue)
    dump=queue[0]
    print(queue)
    dump2=queue.popleft()
    if dump==largest:
         count += 1
         print(dump)
    else:
        queue.append(dump2)
    if target==queue[0]:
        break
print(count)

