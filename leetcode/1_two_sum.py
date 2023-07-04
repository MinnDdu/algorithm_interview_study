# 1. Two Sum

import collections

# My answer
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        result = []
        for i in range(len(nums)):
            diff = target - nums[i]
            left = nums[i + 1:]
            if diff in left:
                result.append(i)
                result.append(left.index(diff) + i + 1)
                break
        return result
    
sol = Solution()
print(sol.twoSum([3,3,2,3,2,3,2], 6))

# Study book - 1. Brute Force (skip)

# Study book - 2. using 'in'
def twoSum(nums: list[int], target: int) -> list[int]:
    for i, n in enumerate(nums):
        complement = target - n
        if complement in nums[i + 1:]:
            return [i, nums[i + 1:].index(complement) + i + 1]
print(twoSum([3,3,2,3,2,3,2], 6))

# Study book - 3. referencing a key with subtracting a first number - hashtable
def twoSum(nums: list[int], target: int) -> list[int]:
    hashtable = collections.defaultdict(int)

    # 값 -> 키 / 인덱스 -> 밸류
    # hashtable - key 중복 없음 -> 중복값이 있으면 가장 마지막 인덱스로 밸류가 저장됨
    for i, n in enumerate(nums):
        hashtable[n] = i
    
    for i, n in enumerate(nums):
        # 주의! - defaultdict 사용시 hashtable[target - n]을 하면 값이 없을때 새로 저장을 해버림... --> .get()쓰기
        if i != hashtable.get(target - n) and target - n in hashtable:
            return [i, hashtable[target - n]]
print(twoSum([-1,-2,-3,-4,-5], -8))

# Study book - 4. improving reference structure (3. 개선)
def twoSum(nums: list[int], target: int):
    hashtable = collections.defaultdict(int)
    for i, n in enumerate(nums):
        if target - n in hashtable:
            return [i, hashtable[target - n]]
        hashtable[n] = i

# Study book - 5. two pointers...? -> 불가(정렬필요 but 정렬시 index 꼬임)
def twoSum(nums: list[int], target: int):
    nums = sorted(nums)
    # 밑의 코드를 사용하려면 nums가 정렬되어있어야함! - 그러나 index가 바뀜... 
    left = 0
    right = len(nums) - 1
    while left < right:
        if nums[left] + nums[right] == target:
            return [left, right]
        elif nums[left] + nums[right] < target:
            left += 1
        elif nums[left] + nums[right] > target:
            right -= 1
    