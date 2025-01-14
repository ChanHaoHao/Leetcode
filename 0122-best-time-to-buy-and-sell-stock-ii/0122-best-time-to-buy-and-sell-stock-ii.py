class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        min_price = prices[0]

        for x in prices[1::]:
            if x<min_price:
                min_price = x
            else:
                res += x-min_price
                min_price = x
        
        return res