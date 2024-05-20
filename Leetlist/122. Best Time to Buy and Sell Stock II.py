# 122. Best Time to Buy and Sell Stock II
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        curr_profit = 0
        buy_price = prices[0]

        for index, price in enumerate(prices[1:],1):
            if price < prices[index-1]:
                #price dropped
                if curr_profit>0:
                    max_profit+=curr_profit
                curr_profit = 0
                buy_price = price
            else:
                #increasing or steady
                curr_profit = price-buy_price
        max_profit+=max(0,curr_profit)
        return max_profit