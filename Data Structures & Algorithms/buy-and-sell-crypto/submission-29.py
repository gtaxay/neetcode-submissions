class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # buy on one day and sell in the future
        # buy on low sell on high
        # two pointers both start at start

        buy, sell = 0, 0
        # no profit
        profit = 0

        # move sell if next is greater than current sell
        # move buy if next is smaller than current buy

        while sell < len(prices):
            if prices[sell] < prices[buy]:
                buy = sell
            else:
                profit = max(profit, prices[sell] - prices[buy])
                sell += 1
 
        return profit


        