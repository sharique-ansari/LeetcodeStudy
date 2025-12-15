# 2110. Number of Smooth Descent Periods of a Stock
# https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/description/

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        # def art(n):
        #     return (n*(n+1))//2
        # prev = prices[0]+1
        # days = 0
        # out = 0
        # for p in prices:
        #     print(p, prev , days, out)
        #     if p == prev-1:
        #         days+=1
        #     else:
        #         out += art(days)
        #         days = 1
        #     prev = p
        # out+=art(days)
        # return out

        out = 1
        days = 1

        for i in range(1, len(prices)):
            if prices[i] == prices[i-1] - 1:
                days += 1
            else:
                days = 1
            out += days
            
        return out
