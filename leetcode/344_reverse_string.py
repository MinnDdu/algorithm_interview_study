# 344 Reverse String
# from typing import List

# My answer
class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s) // 2):
            s[i], s[len(s) - 1 - i] = s[len(s) - 1 -i], s[i]
        
sol = Solution()
sol.reverseString(["A"," ","m","a","n",","," ","a"," ","p","l","a","n",","," ","a"," ","c","a","n","a","l",":"," ","P","a","n","a","m","a"])


# study book - 1. two pointer swapping
def reverseString(s: list[str]) -> None:
    left: int = 0
    right: int = len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

# study book - 2. reverse()
def reverseString(s: list[str]) -> None:
    s.reverse()

# study book - 3. slicing
def reverseString(s: list[str]) -> None:
    # 원래는 s = s[::-1] 도 성공해야 하지만, leetcode에서 이 문제는 시간복잡도를 O(1)로 제한해두어 변수할당에 제약이 생김
    # s[:] = s[::-1] -> 참조가 아닌 값 복사 s[:]를 이용 하여 트릭 - 가장 pythonic한 방법
    s[:] = s[::-1]