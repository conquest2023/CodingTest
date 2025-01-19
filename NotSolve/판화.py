n=int(input())
m=list(input())
cnt=[['.']*n for _ in range(n)]
y=0
x=0
for i in range(len(m)):
    for j in range(n):
        if x<n and y<n:
            if m[i]=='D':
                if cnt[x][y-1]=="|" or cnt[x-1][y]=="-":
                    cnt[x][y]="+"
                    x += 1
                    break
                else:
                    cnt[x][y]="|"
                    x += 1
                    break
            if m[i]=='R':
                if cnt[x-1][y]=="|":
                   cnt[x][y]="+"
                   cnt[x][y + 1] = "-"
                   y += 1
                   break
                else:
                    cnt[x][y] = "-"
                    y += 1
                    break
            if m[i]=='L':
                cnt[x][y-1] = "-"
                y -= 1
                break
            if m[i]=='U':

                if cnt[x][y-1]=="-":
                    cnt[x][y]="+"
                    cnt[x-1][y]="|"
                    x -= 1
                    break
                else:
                    cnt[x - 1][y] = "|"
                    x -= 1
                    break
            print(cnt)
for i in cnt:
    print(i)