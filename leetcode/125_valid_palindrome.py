# 125. Valid Palindrome

# My answer
class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower = s.lower()
        lower = list(filter(str.isalnum, lower))
        lower = ''.join(lower)
        print(lower)
        if len(lower) == 1:
            return True
        
        for i in range(len(lower) // 2):
            if lower[i] != lower[len(lower) - 1 - i]:
                return False
        return True
sol = Solution()
sol.isPalindrome("A man, a plan, a canal: Panama")

# study book - 1. w/ list

