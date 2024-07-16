class SmallestInfiniteSet:

    def __init__(self):
        self.heap = list(range(1,1001))
        self.set = set(self.heap)
        heapq.heapify(self.heap)

    def popSmallest(self) -> int:
        tmp = heapq.heappop(self.heap)
        self.set.remove(tmp)
        return tmp

    def addBack(self, num: int) -> None:
        if num not in self.set:
            heapq.heappush(self.heap, num)
            self.set.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)