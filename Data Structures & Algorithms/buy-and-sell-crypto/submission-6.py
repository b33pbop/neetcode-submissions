class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        best = 0

        for price in prices[1:]:
            if price < buy:
                buy = price

            elif price > buy and price - buy > best:
                best = price - buy

        return best
        