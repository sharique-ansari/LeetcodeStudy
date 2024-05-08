# 35. Search Insert Position
# https://leetcode.com/problems/search-insert-position/description/
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start < end:
            mid =  int((start+end)/2)

            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                end = mid-1
                pass
            elif nums[mid]<target:
                start = mid+1
                pass
        if nums[start] >= target:
            return start
        elif nums[start] < target:
            return start+1