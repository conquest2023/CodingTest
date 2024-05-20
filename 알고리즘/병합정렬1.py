def merge_sort(arr):
    def sort(low, high):
        global a,m
        if high - low < 2:
            return
        mid = (low + high) // 2
        sort(low, mid)
        a+=1
        sort(mid, high)
        a+=1
        merge(low, mid, high)
        a+=1
        return a
    def merge(low, mid, high):
        temp = []
        l, h = low, mid
        while l < mid and h < high:
            if arr[l] < arr[h]:
                temp.append(arr[l])

                l += 1
            else:
                temp.append(arr[h])
                h += 1

        while l < mid:

            temp.append(arr[l])
            l += 1
        while h < high:

            temp.append(arr[h])
            h += 1

        for i in range(low, high):
            arr[i] = temp[i - low]
        print(temp)
    return sort(0, len(arr))

n,m=map(int,input().split())

A=list(map(int,input().split()))
a=0
if merge_sort(A)>m:
    print()