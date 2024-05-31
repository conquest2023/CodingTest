from queue import PriorityQueue
Sum=0
total=0
n=int(input())
queue=PriorityQueue()
for i in range(n):
    card=int(input())
    queue.put(card)
while queue.qsize()>1:
    data1=queue.get()
    data2=queue.get()
    Sum=data1+data2
    total+=Sum
    queue.put(total)
print(total)