class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]
        # multiplying by 2 just adds a 0 => ans[n] = ans[2n]
        # ans[2n+1] = ans[n]+1, the +1 is caused by the odd number
        for x in range(1, n+1):
            ans.append(ans[x>>1]+x%2)
        
        return ans