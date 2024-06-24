"""
n=int(input())
cnt=list(map(int,input().split()))
cnt2=[]
count=1
count2=1
for i in range(1,n):
    if cnt[i-1]<cnt[i]:
        count+=1
        cnt2.append(count2)
        count2=1
    elif cnt[i - 1]==cnt[i]:
         count += 1
         count2 += 1
    else:
         cnt2.append(count)
         count = 1
         count2+=1

print(max(cnt2))
"""
"""개선된 코드"""
N = int(input())
li = list(map(int, input().split()))
dp1, dp2 = [1]*N, [1]*N
for i in range(1, N):
    if li[i] <= li[i-1]:
        dp1[i] = max(dp1[i], dp1[i-1]+1)
    if li[i] >= li[i-1]:
        dp2[i] = max(dp2[i], dp2[i-1]+1)
print(max(max(dp1), max(dp2)))