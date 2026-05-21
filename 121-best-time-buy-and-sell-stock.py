class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest_min = prices[0]
        for i in range(len(prices)):
            if prices[i] < lowest_min:
                lowest_min = prices[i]
            cur_profit = prices[i] - lowest_min
            if cur_profit > max_profit:
                max_profit = cur_profit
        return max_profit