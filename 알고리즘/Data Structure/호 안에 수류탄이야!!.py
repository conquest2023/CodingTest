N=int(input())
people=list(map(int,input().split()))
count=0
if N==1:
    print("권병장님, 중대장님이 찾으십니다")
    exit()
width = list(map(int, input().split()))
for i in range(N):
    for j in range(i+1,len(width)+1):
        if   people[j]-people[i]>width[i]:
             count+=1
        if   width[i]>=max(people)-people[i] or  width[i]>=max(people)-min(people):
            print("권병장님, 중대장님이 찾으십니다")
            exit()
        break
if count==0:
   print("권병장님, 중대장님이 찾으십니다")
else:
    print("엄마 나 전역 늦어질 것 같아")
