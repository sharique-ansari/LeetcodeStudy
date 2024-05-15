# 1219. Path with Maximum Gold
# https://leetcode.com/problems/path-with-maximum-gold/description/


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        # will try recursion (There are at most 25 cells containing gold.)

        def rec(point_x, point_y):

            if point_x < 0 or point_y < 0 or point_x == m or point_y == n or grid[point_x][point_y] == 0:
                return 0

            org_val = grid[point_x][point_y]
            grid[point_x][point_y] = 0
            out = max(rec(point_x + 1, point_y), rec(point_x - 1, point_y), rec(point_x, point_y - 1),
                      rec(point_x, point_y + 1))
            grid[point_x][point_y] = org_val
            return org_val + out

        max_sum = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    # try recursing over all values starting from this
                    sum_rec = rec(i, j)
                    pass
                    if sum_rec > max_sum:
                        max_sum = sum_rec
        return max_sum