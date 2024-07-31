class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # TLE O^2
        # n = len(prices)
        # if n==1:
        #     return 0
        # elif n==2:
        #     return max(prices[1]-prices[0]-fee, 0)

        # max_storage = [0]*n
        # for i in range(n):
        #     for j in range(i+1, n):
        #         profit = prices[j]-(prices[i]+fee)
        #         if i>1:
        #             max_storage[j] = max(max_storage[j], profit+max_storage[i-1])
        #         else:
        #             max_storage[j] = max(max_storage[j], profit)

        #     if i+1<n:
        #         max_storage[i+1] = max(max_storage[i], max_storage[i+1])

        # return max(max_storage)
        
        buy = -float("inf")
        sell = 0
        for price in prices:
            # buy stores the best profit when a day ends with buying
            # it will be the previous buy profit or sell-current price (means you bought that day)
            buy = max(buy, sell-price)
            # sell stores the best profit when a day ends with selling
            # it will be the previous sell profit or buy+current price-fee (buy contains the previous sold)
            # doesn't need to consider buy and sell on the same day, becaues it will be guarenteed to be less than previous sell price
            sell = max(sell, buy+price-fee)
        
        return sell