class Solution:
    def climbStairs(self, n: int) -> int:
        # ans=0

        # def multi(num):
        #     ans=1
        #     for x in range(2, num+1):
        #         ans*=x
        #     return ans

        # m=n//2
        # for x in range(m+1):
        #     tmp=1
        #     ones=n-x*2
        #     ans+=multi(ones+x)/(multi(ones)*multi(x))
        # return int(ans)

        #Dynamic Programming, bottom-up method
        first, second=1, 1
        for x in range(n-1):
            first, second=first+second, first
        return first