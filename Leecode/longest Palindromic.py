class Solution(object):
    def longestPalindrome(self, s):
        length = len(s)
        word = []
        cnt = []
        half = len(s) // 2
        if length % 2 == 0:
            for i in range(1, half + 1):
                if s[-i] == s[i - 1]:
                    word.append([s[-i], s[i - 1]])
        else:
            for i in range(1, half + 1):
                if s[-i] == s[i - 1]:
                    word.append([s[-i], s[half], s[i - 1]])
        frist = 0
        end = len(word) - 1
        return word[frist:end + 1]



