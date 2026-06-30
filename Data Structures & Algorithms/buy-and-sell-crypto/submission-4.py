class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max_profit = 0

        # for i in range(0, len(prices)):
        #     for j in range(i+1, len(prices)):
        #         diff = prices[j] - prices[i]
        #         max_profit = max(max_profit, diff)
                
        # return max_profit

        min_price = float('inf')
        max_profit = 0

        for i in prices:
            min_price = min(min_price, i)
            diff = i - min_price
            max_profit = max(max_profit, diff)
                
        return max_profit           
                