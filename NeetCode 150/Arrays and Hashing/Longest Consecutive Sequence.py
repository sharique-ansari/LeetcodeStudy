# 128. Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/description/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Solving using recursion and memoization
        if not nums:
            return 0
        set_nums = set(nums)
        out_dic = {}

        def rec_find(n):
            if n - 1 not in set_nums:
                out_dic[n] = 1
                return out_dic[n]
            if n - 1 in out_dic:
                out_dic[n] = 1 + out_dic[n - 1]
                return out_dic[n]
            out_dic[n] = 1 + rec_find(n - 1)
            return out_dic[n]

        for num in nums:
            out = rec_find(num)

        return max(out_dic.values())