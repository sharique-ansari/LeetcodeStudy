# https://leetcode.com/problems/count-the-number-of-computer-unlocking-permutations/description/?source=submission-ac
# 3577. Count the Number of Computer Unlocking Permutations

class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        # base_complexity = complexity[0]
        mod = 1000000007

        # for comp in complexity[1:]:
        #     if comp <= base_complexity:
        #         return 0
        # return math.factorial(len(complexity)-1)%mod

        
        if complexity[0] >= min(complexity[1:]):
            return 0
        return math.factorial(len(complexity)-1)%mod
