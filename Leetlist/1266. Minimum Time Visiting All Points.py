# 1266. Minimum Time Visiting All Points
# https://leetcode.com/problems/minimum-time-visiting-all-points/description/?envType=daily-question&envId=2026-01-12

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:

        time = 0

        prev = points[0]

        for point in points[1:]:
            time += max(abs(point[0]-prev[0]), abs(point[1]-prev[1]))
            prev = point
        return time
