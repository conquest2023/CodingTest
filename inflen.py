def recursion(m,i,r):
    global cnt
    cnt+=1
    if(i>=r):
        return 1
    elif m[i]!=m[r]:
        return 0
    else:
        return recursion(m,i+1,r-1)
def isPalindrome(m):
    return recursion(m,0,len(m)-1)

n=int(input())
for i in range(n):
    cnt=0
    print(isPalindrome(list(input())),cnt)