# 121. Best Time to Buy and Sell Stock - Easy

import sys

# My answer
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min = prices[0]
        profit = 0 
        for i in range(1, len(prices)):
            if prices[i] < min:
                min = prices[i]
            if prices[i] - min > profit:
                profit = prices[i] - min
        return profit
            
    
sol = Solution()
print(sol.maxProfit([2,4,1]))
print(sol.maxProfit([7,1,5,3,6,4]))

# Study book - 1. Brute Force -> Time Out
def maxProfit(prices: list[int]) -> int:
    result = 0
    for i in range(len(prices) - 1):
        for j in range(i + 1, len(prices)):
            if prices[j] - prices[i] > result:
                result = prices[j] - prices[i]
    return result
print(maxProfit([7,1,5,3,6,4]))

# Study book - 2. updating value / pointer points to current value
def maxProfit(prices: list[int]) -> int:
    profit = 0
    min_price = sys.maxsize
    for price in prices:
        min_price = min(price, min_price)
        profit = max(profit, price - min_price)
    return profit


