n=int(input())
m=list(map(int,input().split()))
cnt=[False]*111111
count=0
Max=0
for i in m:
    if not  cnt[i]:
       cnt[i]=True # True로 하는게 더 빠름
       count+=1
    elif cnt[i]:
         count-=1
    Max=max(Max,count)
print(Max)

#일반적으로 list를 만들어서 푸는 것 보다는 특정 값으로 풀이하는게 시간, 메모리를 적게 사용한다
"""n = int(input())
nList = list(map(int, input().split()))
ans = 0
cnt = 0
menu = [False] * 111111

for num in nList:
    if not menu[num]:  # 한번도 안 나왔다면
        cnt += 1
        menu[num] = True
    else:
        cnt -= 1
        menu[num] = False

    ans = max(ans, cnt)  # 붙어있는 스티커 최대 개수 업데이트

print(ans)"""