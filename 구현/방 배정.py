N,K=map(int,input().split())
cnt=[]
cnt1=[]
cnt3=[]
count=0
count2=0
count3=0
count4=0
pos=0
count5=0
for i in range(N):
    S,Y=map(int,input().split())
    cnt.append([S,Y])
cnt.sort()
for i in range(len(cnt)):
    if cnt[i][1]<=2:
       cnt1.append(cnt[i])
       if len(cnt1)==K:
           pos+=1
           cnt1.clear()
    elif  cnt[i][1]>=3 and cnt[i][1]<=4:
           if cnt[i][0]==1:
               count += 1
               if count == K:
                   count = 0
                   pos += 1
           else:
                count2+=1
                if count2 == K:
                    count2 = 0
                    pos += 1
    else:
         cnt3.append(cnt[i])
for i in range(len(cnt3)):
    if cnt3[i][0]==0:
        count3+=1
        if count3==K:
            count3=0
            pos+=1
    else:
         count4+=1
         if count4==K:
            count4=0
            pos+=1
if count3>0 and count3<K:
    count3=1
if count2>0 and count2<K:
    count2=1
if count>0 and count<K:
    count=1
if count4>0 and count4<K:
    count4=1
if len(cnt1)>0 and len(cnt1)<K:
      count5=1
print(pos+count3+count4+count+count2+count5)

