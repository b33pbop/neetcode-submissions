class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float('inf')
        best = 0

        for price in prices:
            if price < buy:
                buy = price

            elif price > buy and price - buy > best:
                best = price - buy

        return best
        