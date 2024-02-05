class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans, tmp = 0, 0

        for x in gain:
            tmp += x
            if tmp>ans:
                ans = tmp
        
        return ans