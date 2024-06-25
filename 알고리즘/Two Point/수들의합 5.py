"""
import sys
Num=int(sys.stdin.readline())
cnt=[i for i in range(1,Num+1)]
left=0
right=0
count=0
target=Num
while right!=Num:
      if sum(cnt[left:right])<target:
          right+=1
      elif sum(cnt[left:right])>target:
           left+=1
      else:
          count+=1
          left+=1
          right+=1
print(count+1)
"""
import sys
input = sys.stdin.readline
N = int(input())
start = 1
end = 1
total = 1
count = 1  ## 자기 자신 포함

## 1, 2만 예외처리
if N == 1 or N == 2:
  print(1)
  sys.exit()

## 반복하며 카운트, end가 굳이 N까지 갈필요 없다고 생각해서 반복조건을 저런식으로 함.
while end < N//2 + 2:
  if total == N:
    count += 1
    end += 1
    total = total + end
  elif total < N:
    end += 1
    total = total + end
  else:
    total = total - start
    start += 1
print(count)