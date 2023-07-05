# 42. Trapping Rain Water - Hard
import collections
import re

# My answer - fail to solve it
# Study book - 1. Two pointers
class Solution:
    def trap(self, height: list[int]) -> int:
        rain = 0
        left, right = 0, len(height) - 1
        left_max = height[left]
        right_max = height[right]

        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            if left_max <= right_max:
                rain += left_max - height[left]
                left += 1
            else: # left_max > right_max
                rain += right_max - height[right]
                right -= 1

        return rain
                    
sol = Solution()
# print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
# print(sol.trap([4,2,0,3,2,5]))

# Study book - 2. Stack
def trap(height: list[int]) -> int:
    stack = []
    rain = 0

    for i in range(len(height)):
        # Encountering inflection point (변곡점)
        while stack and height[i] > height[stack[-1]]:
            top = stack.pop()

            if not len(stack):
                break

            distance = i - stack[-1] - 1
            waters = min(height[i], height[stack[-1]]) - height[top]
            rain += distance * waters
        stack.append(i)
    return rain
print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))