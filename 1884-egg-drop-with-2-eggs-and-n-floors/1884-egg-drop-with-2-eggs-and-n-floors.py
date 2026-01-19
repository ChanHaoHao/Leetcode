class Solution:
    def twoEggDrop(self, n: int) -> int:
        egg = 1
        while n>0:
            n -= egg
            egg += 1
        return egg-1