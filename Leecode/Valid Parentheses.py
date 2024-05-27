class Solution(object):
    def isValid(self, s):
       stack=[]
       table={')':'(','}':'{',']':'[',}
       for c in s:
         if c not in table:
            stack.append(c)
         elif not stack or table[c]!=stack.pop():
              return False
       return len(stack)==0