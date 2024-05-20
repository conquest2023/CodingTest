import sys
n=int(sys.stdin.readline())
m=list(map(int,sys.stdin.readline().split()))
arr2=sorted(set(m))
arr={arr2[i]:i for i in range(len(arr2))}
print(arr)
for i in m:
    print(arr[i],end=' ')

