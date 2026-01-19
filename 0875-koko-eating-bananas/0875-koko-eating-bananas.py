class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eat(speed):
            hour = 0
            for p in piles:
                hour += p//speed
                if p%speed:
                    hour += 1

            return hour

        l, r = 1, max(piles)
        ans = r

        while l<=r:
            mid = (l+r)//2

            hours = eat(mid)
            if hours<=h:
                ans = min(ans, mid)
                r = mid - 1
            else:
                l = mid + 1
        

        return ans