
def Binary_search(array,target,start,end):
    while start<=end:
      
      mid=(start+end)//2
      
      if array[mid]==target:
          return mid 
      elif array[mid]>target:
          end=mid-1
      else:
          start=mid+1
    return None    
N = int(input())
card = list(map(int, input().split()))
card.sort()
M = int(input())
other = list(map(int, input().split()))


for i in range(M):
    if Binary_search(card,other[i],0,N-1) is not None:
        print(1,end=' ')
    else:
        print(0,end=' ')    


