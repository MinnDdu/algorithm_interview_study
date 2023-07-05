# 15. 3Sum - Medium

# Study book - 1. Two pointers
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while left < right:
                candidate = nums[i] + nums[left] + nums[right]
                if candidate == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif candidate < 0:
                    left += 1
                elif candidate > 0:
                    right -= 1
        return result
sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))