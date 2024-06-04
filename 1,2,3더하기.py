n=int(input())

for i in range(n):
    target=int(input())
    if target==1:
        print(1)
    elif target==2:
        print(2)
    else:
         cnt =[0]*(target+1)
         while True:
            cnt[1] = 1
            cnt[2] = 2
            cnt[3] = 4
            for i in range(4,len(cnt)):
                cnt[i]=cnt[i-3]+cnt[i-2]+cnt[i-1]
            print(cnt[-1])
            break

