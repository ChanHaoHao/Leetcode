class Solution:
    def maxProduct(self, n: int) -> int:
        ans = 0
        first_num = n%10
        n = n//10
        while n!=0:
            tmp = n%10
            n = n//10
            if first_num*tmp > ans:
                ans = first_num*tmp
                if ans==81:
                    return ans
            if tmp>first_num:
                first_num = tmp
        
        return ans
            