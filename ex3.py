n=int(input())
cnt=[]
cnt2=[]
for i in range(n):
    a,b=list(input().split())
    cnt.append([a,b]) 
for i in range(n):
    count=1
    for j in range(n):
        if cnt[i][0]<cnt[j][0] and cnt[i][1]<cnt[j][1]:
              count+=1
    cnt2.append(count)
for i in cnt2:
     print(i,end=" ")        
n = int(input())
people = []
for _ in range(n):
    people.append(list(map(int, input().split())))
for i in people:
    ranking = 1
    for j in people:
        if i[0] < j[0] and i[1] < j[1]:
            ranking += 1
    print(ranking, end=" ")            