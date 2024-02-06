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
    
    # Study book - 1. Mapping Talbe by dictionary
    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }

        for char in s:
            if char in table:
                stack.append(char)
            elif table[char] != stack.pop():
                return False
            elif not stack or table[char] != stack.pop():
                return False
        return len(stack) == 0

