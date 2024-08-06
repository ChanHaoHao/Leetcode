class StockSpanner:

    def __init__(self):
        self.stack = []
        self.day = 0

    def next(self, price: int) -> int:
        self.day += 1

        # make the stack in a decreasing order
        # pop all the prices that are less than todays
        while (self.stack and self.stack[-1][0]<=price):
            self.stack.pop()
            
        # if today's price is the greatest
        if not self.stack:
            ans = self.day
        else:
            ans = self.day-self.stack[-1][1]
        self.stack.append([price, self.day])

        return ans


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)