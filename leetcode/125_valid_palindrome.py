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
def isPalindrome(s: str) -> bool:
    preprocess = []
    for c in s:
        if c.isalnum():
            preprocess.append(c.lower())
    
    while len(preprocess) > 1:
        # List.pop(0) -> O(n)
        if preprocess.pop(0) != preprocess.pop():
            return False
    return True
isPalindrome("A man, a plan, a canal: Panama")

# study book - 2. w/ deque
import collections
def isPalindrome(s: str) -> bool:
    deque = collections.deque()
    for c in s:
        if c.isalnum():
            deque.append(c.lower())
    while len(deque) > 1:
        # Deque.popleft() -> O(1)
        if deque.popleft() != deque.pop():
            return False
    return True

# study book - 3. w/ regex and slicing
# slicing은 굉장히 효율적임 - 내부적으론 C언어로 구현되어있기때문
import re
def isPalindrome(s: str) -> bool:
    s = s.lower()
    s = re.sub('[^0-9a-z]', '', s)
    return s == s[::-1]