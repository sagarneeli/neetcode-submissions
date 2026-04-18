class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        profit = 0

        while right < len(prices):
            buy, sell = prices[left], prices[right]
            if buy < sell:
                profit = max(profit, sell - buy)
            else:
                left = right
            right += 1
        
        return profit

        