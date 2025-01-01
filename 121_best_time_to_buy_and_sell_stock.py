# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Given an array where the ith element is the price of a stock on day i, and only one transaction (buy and sell) is allowed,
# design an algorithm to find the maximum profit.

# Track the minimum price (the maximum loss at any point) and calculate the maximum profit
# as the difference between the current price and the minimum price.
# Time complexity: O(n)
# Space complexity: O(1)

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = float('-inf')     # maximum cash balance after buying a stock
        sell = 0                # maximum cash balance after buying and selling a stock
        for price in prices:
            buy = max(-price, buy)          # max of buying earlier or now
            sell = max(price + buy, sell)   # max of selling earlier or now
        return sell