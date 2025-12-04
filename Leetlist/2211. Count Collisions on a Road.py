# 2211. Count Collisions on a Road
# https://leetcode.com/problems/count-collisions-on-a-road/description/?envType=daily-question&envId=2025-12-04
class Solution:
    def countCollisions(self, directions: str) -> int:
        # out = 0
        # stack = []
        # for d in directions:
        #     if d == 'S':
        #         while stack and stack[-1]=='R':
        #             stack.pop()
        #             out+=1
        #         stack.append('S')
        #     elif d=='L':

        #         if stack and stack[-1]=='S':
        #             out+=1
        #             continue
        #         elif stack and stack[-1]=='R':
        #             stack.pop()
        #             out+=2
        #             while stack and stack[-1] == 'R':
        #                 stack.pop()
        #                 out += 1
        #             stack.append('S')

        #     else:
        #         stack.append("R")
        # return out
        trimmed = directions.lstrip('L').rstrip('R')
        # print(directions[i:j+1])
        return len(trimmed) - trimmed.count('S')

        
