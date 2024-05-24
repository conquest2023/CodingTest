class Solution(object):
    def isPalindrome(self, s):
        pos = []
        for i in s:
            if i.isalnum():
                pos.append(i.lower())

        if pos == pos[::-1]:
            return True
        else:
            return False
"""
팰린드롬 여부 판별
while len(strs)>1:
    if sts.pop(0) !=sts.pop():
        return False
        
    return True
"""

"""
Deque로 구현
 def isPalindrome(self, s):
    strs:Deque=collcetions.deque()
    
    while len(sts)>1:
        if strs.poplfets()!=strs.pop():
            return False
        return True
"""
