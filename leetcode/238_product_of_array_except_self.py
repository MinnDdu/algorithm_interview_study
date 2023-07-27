# 238. Product of Array Except Self - medium

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

# My answer - Space Complexity O(1) 안됨
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = []
        left = []
        right = []
        for i, n in enumerate(nums):
            if len(left) == 0:
                left.append(n)
            else:
                left.append(left[i-1] * n)
        
        for i, n in enumerate(nums[::-1]):
            if len(right) == 0:
                right.append(n)
            else:
                right.append(right[i-1] * n)
        right = right[::-1]

        for i in range(len(left)):
            if i == 0:
                result.append(right[i + 1])
            elif i == len(left) - 1:
                result.append(left[i - 1])
            else:
                result.append(left[i - 1] * right[i + 1])

        return result
s1 = Solution()
print(s1.productExceptSelf([4,3,2,1,2]))
        
# Study book - 1. w/ Space Complexity O(1)
def productExceptSelf(nums: list[int]) -> list[int]:
    result = [] # output space is not considered for space complexity

    p = 1
    for i in range(len(nums)):
        result.append(p)
        p = p * nums[i]
    
    p = 1
    for i in range(len(nums) - 1, -1, -1):
        result[i] *= p
        p = p * nums[i]

    return result