# 561 Array Partition 1 - Easy

# My answer
class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        nums.sort()
        result: int = 0
        for i in range(0, len(nums), 2):
            result += nums[i]

        return result
    
s = Solution()
print(s.arrayPairSum([6,2,6,5,1,2]))

# Study book - 1. Even index summation w/ enumerate
def arrayPartitionSum(nums: list[int]) -> int:
    nums.sort()
    result = 0
    for i, n in enumerate(nums):
        if i % 2 == 0:
            result += n
    return result

# Study book - 2. Pythonic way -> list slicing
def arrayPartitionSum(nums: list[int]) -> int:
    return sum(sorted(nums)[::2])