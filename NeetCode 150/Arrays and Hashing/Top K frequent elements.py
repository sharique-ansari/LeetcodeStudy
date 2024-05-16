# 347. Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/description/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_nums = Counter(nums)

        out = sorted([(i,j) for i,j in count_nums.items()], key = lambda a:a[1], reverse = True)[:k]
        return [i for i,j in out]