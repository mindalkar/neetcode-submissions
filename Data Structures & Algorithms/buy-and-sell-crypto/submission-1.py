class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        i , j = 0, 1

        while j < len(prices):
            if prices[j] > prices[i]:
                res = max(prices[j] - prices[i], res)
            else:
                i = j
            j += 1

        return res

        