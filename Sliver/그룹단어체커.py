"""내가 푼 코드
n=int(input())
cnt=[]
count=0
for i in range(n):
    m=list(input())
    cnt.append(m)
for i in cnt:
    x=0
    if" "len(i)==1 or len(i)==2 or len(set(i))==1:
        count+=1
    elif i[x] not in i[x:] or i[x] not in i[x+1:]:
                count+=1
print(count)
"""
"""개선되누코드"""
n = int(input())
ans = 0
for _ in range(n):
    array = input()
    for j in range(len(array)):
        if j != len(array) - 1:
            if array[j] == array[j + 1]:
                continue
            elif array[j] in array[j + 1:]:
                break
        else:
            ans += 1
print(ans)