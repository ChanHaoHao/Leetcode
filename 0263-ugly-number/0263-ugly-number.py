class Solution:
    def isUgly(self, n: int) -> bool:
        if n==0:
            return False
            
        primeFactors = [2, 3, 5]
        while n!=1:
            thres = False
            for x in primeFactors:
                if n%x==0:
                    thres = True
                    n /= x
            
            if not thres:
                return False
        return True