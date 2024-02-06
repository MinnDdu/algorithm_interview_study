# 316. Remove Duplicate Letters - Medium

class Solution:
    # My answer - Wrong
    def removeDuplicateLetters(self, s: str) -> str:
        if len(s) == 1:
            return s
        lst = list(s)
        unique = list(set(lst))
        return "".join(unique)

    # Study book - 1. Recursion
    def removeDuplicateLetters(self, s: str) -> str:
        lst = sorted(set(s))
        if s == '':
            return ''

        for c in lst:
            suffix = s[s.index(c):]
            if set(suffix) == set(s):
                return c + self.removeDuplicateLetters(suffix.replace(c, ''))



s = 'cbacdcbc'
ss = Solution()
print(ss.removeDuplicateLetters(s))
