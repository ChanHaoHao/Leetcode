class Solution:
    def getLucky(self, s: str, k: int) -> int:
        ans = 0
        # perform the convert and transform at the same time, 
        # since we are guarenteed to transform once
        for x in s:
            num = ord(x)-96
            while num!=0:
                ans += num%10
                num = num//10
        
        # perform the transform greater than 1
        for x in range(1, k):
            tmp = 0
            while ans!=0:
                tmp += ans%10
                ans = ans//10
            ans = tmp
        
        return ans