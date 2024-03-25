class RecentCounter:

    def __init__(self):
        # this stores the previous pings
        self.prev_ping = []

    def ping(self, t: int) -> int:
        self.prev_ping.append(t)
        while len(self.prev_ping)>0:
            if t-self.prev_ping[0]>3000:
                self.prev_ping.pop(0)
            else:
                return len(self.prev_ping)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)