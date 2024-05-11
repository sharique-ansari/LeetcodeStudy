# https://leetcode.com/problems/maximum-points-inside-the-square/
# 3143. Maximum Points Inside the Square
class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        dic = {}
        max_distance = float("inf")
        out = 0
        for point, name in zip(points, s):
            print(point, name)
            if name in dic:
                current_value = max(abs(point[0]), abs(point[1]))
                prev_value = dic[name]
                dic[name] = min(current_value, prev_value)
                max_distance = min(max_distance, max(current_value, prev_value) - 1)

            else:
                if max(point) <= max_distance:
                    dic[name] = max(abs(point[0]), abs(point[1]))
        for value in dic.values():
            if value <= max_distance:
                out += 1
        print(dic, max_distance)
        return out