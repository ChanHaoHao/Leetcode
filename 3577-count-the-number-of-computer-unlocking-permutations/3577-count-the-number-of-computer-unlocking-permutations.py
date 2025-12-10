class Solution(object):
    def countPermutations(self, complexity):
        """
        :type complexity: List[int]
        :rtype: int
        """
        module = 10**9+7
        first = complexity[0]

        for c in complexity[1:]:
            if c<=first:
                return 0
        
        ans = 1
        for i in range(2, len(complexity)):
            ans = (ans * i) % module
        
        return ans