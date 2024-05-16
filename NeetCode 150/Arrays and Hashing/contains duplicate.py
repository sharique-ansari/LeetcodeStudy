# 217. Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/description/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # # Method 1
        # if len(nums)==len(set(nums)):
        #     return False
        # return True

        # Method 2
        set_nums = set()
        for i in nums:
            if i in set_nums:
                return True
            else:
                set_nums.add(i)
        return False