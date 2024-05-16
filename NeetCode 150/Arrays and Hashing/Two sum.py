# 1. Two Sum
# https://leetcode.com/problems/two-sum/description/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic_nums = {}

        for index, num in enumerate(nums):
            if target-num in dic_nums:
                return [index,dic_nums[target-num]]
            else:
                dic_nums[num] = index