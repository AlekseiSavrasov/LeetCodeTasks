# https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums, target: int):
        for i, k in enumerate(nums):
            if target-k in nums[i+1:]:
                return [i, len(nums[:i+1])+nums[i+1:].index(target - k)]

s = Solution()
res = s.twoSum(nums = [1, 3, 2, 3], target = 6)
print(res)
