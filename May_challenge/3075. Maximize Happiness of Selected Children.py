# https://leetcode.com/problems/maximize-happiness-of-selected-children/

# Sort + greedy approach
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse = True)
        out = 0
        for i in range(k):
            out += max(0, happiness[i] - i)
        return out