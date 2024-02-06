# 20. Valid Parentheses - Easy


class Solution:
    # My answer
    def isValid(self, s: str) -> bool:
        stack = []
        open = ['(', '{', '[']
        close = [')', '}', ']']
        for c in s:
            if c in open:
                stack.append(c)
            elif c in close:
                if stack == []:
                    return False
                pair = stack.pop()
                if open.index(pair) != close.index(c):
                    return False
        if stack == []:
            return True