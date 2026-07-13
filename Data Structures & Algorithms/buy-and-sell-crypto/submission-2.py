class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highest_profit = 0

        l = 0
        r = 1

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                highest_profit = max(highest_profit, profit)
            else:
                l = r
            
            r += 1

            

        return highest_profit


        