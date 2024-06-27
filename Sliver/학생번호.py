n=int(input())
cnt=[]
count=0
words=set()
for i in range(n):
    m=list(input())
    m=list(reversed(m))
    cnt.append(m)
num=len(cnt[0])
for i in range(len(cnt)):
    idx=0
    for j in range(i+1,len(cnt)):
        if cnt[i][0]==cnt[j][0]:
             words.add(cnt[i][0])
             count+=1
             while num!=0:
                 num-=1
                 idx+=1
                 if idx==len(cnt[0]):
                     break
                 if cnt[i][idx]==cnt[j][idx]:
                     words.add(cnt[i][idx])
                 else:
                      break
print(len(words)+1)
"""
n=int(input())
nums=[]
for _ in range(n):
    nums.append(str(input()))
for i in range(1, len(nums[0])+1):
    results=[]
    for j in range(n):
        if nums[j][-i:] in results:
            break
        else:
            results.append(nums[j][-i:])
    if len(results)==n:
        print(i)
        break
"""