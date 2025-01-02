N=list(input())

if len(set(N))==len(N) or  len(set(N))==len(N)-1:
    print("I'm Sorry Hansoo")
for i in range(1,(len(N)//2)+1):
    if N[i-1]!=N[-i]:
        N[-i]= N[i-1]
    if N[:len(N)//2] ==N[len(N)//2:]:
        break
print(N)