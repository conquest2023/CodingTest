nums=[2,7,11,15]
target=9
cnt=[]
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==target:
            cnt.append([i,j])
            break
print(cnt)


"""개선된 코드"""

nums=[2,7,11,15]
target=9
nums_map={}
for i,num in enumerate(nums):
    nums_map[num]=i

for i,num in enumerate(nums):
    if target-num in nums_map and i !=nums_map[target-num]:
        return nums.index(num),nums_map[target -num]

"""투 포인터  """

left,right=0,len(nums)-1

while not left==right:  """시간 복잡도 0(n)"""
     if nums[left]+nums[right]<target:
         left+=1
     elif nums[left] +nums[right]>target:
         right-=1
     else:
         return left,right