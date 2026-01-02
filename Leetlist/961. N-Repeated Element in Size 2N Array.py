# 961. N-Repeated Element in Size 2N Array
# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/description/?envType=daily-question&envId=2026-01-02

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        seen = set()

        for i in nums:
            if i in seen:
                return i
            else:
                seen.add(i)
        
