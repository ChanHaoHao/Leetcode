class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        history =set()
        history.add(n)

        while True:
            next_n = 0
            while n>0:
                next_n += (n%10)**2
                n = n//10
            if next_n==1:
                return True
            if next_n in history:
                return False
            history.add(next_n)
            n = next_n
        