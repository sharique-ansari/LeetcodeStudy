# 3432. Count Partitions with Even Sum Difference
# https://leetcode.com/problems/count-partitions-with-even-sum-difference/description/

class Solution:
    def countPartitions(self, nums: List[int]) -> int:

        left = nums[0]
        right = sum(nums[1:])
        if (left - right)%2==0:
            return len(nums)-1
        
        return 0
