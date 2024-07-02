a,b=(map(int,input().split()))
target = b
count = 1
while True:
    if target==a:
        break
    if target % 10 == 1:
      target=target//10
      count += 1
    else:
        target = target//2
        count += 1
    if a>target:
        print(-1)
        break
if target==a:
    print(count)

