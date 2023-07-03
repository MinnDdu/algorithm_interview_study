# 1. Two Sum

# My answer
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        result = []
        for i in range(len(nums)):
            diff = target - nums[i]
            left = nums[i+1:]
            if diff in left:
                result.append(i)
                result.append(left.index(diff) + i + 1)
                break
        return result
    
sol = Solution()
print(sol.twoSum([3,3,2,3,2,3,2], 6))

# Study book - 1. 