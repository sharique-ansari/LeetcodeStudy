# https://leetcode.com/problems/check-if-grid-satisfies-conditions/
# 3142. Check if Grid Satisfies Conditions
class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        for i in range(len(grid) - 1):
            for j in range(len(grid[0])):
                if grid[i][j]!=grid[i+1][j]:
                    return False
        for i in range(len(grid)):
            for j in range(len(grid[0]) - 1):
                if grid[i][j] == grid[i][j+1]:
                    return False
        return True