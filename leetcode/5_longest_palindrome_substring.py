# 5. Longest Palindrome Substring
import collections

# Study book - 1. two pointers sliding window
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2 or s == s[::-1]:
            return s
        
        def expand(s: str, left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        
        result = ''
        # 의문점 -> 왜 len(s) - 1?
        for i in range(len(s) - 1):
            result = max(result, expand(s, i, i+1), expand(s, i, i+2), key=len)
        
        return result

sol = Solution()
print(sol.longestPalindrome("babad"))


        