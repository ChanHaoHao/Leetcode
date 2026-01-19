class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 1, x
        ans = x
        
        while l<=r:
            mid = (l+r)//2

            if mid**2>x:
                r = mid - 1
            else:
                ans = mid
                l = mid + 1
        
        return ans