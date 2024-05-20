# 283. Move Zeroes
# https://leetcode.com/problems/move-zeroes/description/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        pointer = 0

        for index, value in enumerate(nums):
            if value:
                nums[pointer] = value
                pointer += 1
        nums[pointer:] = [0] * len(nums[pointer:])