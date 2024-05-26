nums = [1,4,3,2]
class Solution(object):
    def arrayPairSum(self, nums):
       nums.sort()
       box=[]
       count=0
       size=len(nums)//2
       for i in range(1,size+1):
           count2=min(nums[(2*(i-1)):(2*i)])
           count+=count2
       return count

"""개선된 코드"""

sum=0
pair=[]
nums.sort()
for n in nums:
    pair.append(n)
    if len(pair)==2:
        sum+=min(pair)
        pair=[]
