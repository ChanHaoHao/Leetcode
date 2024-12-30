class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        module = 10**9+7
        dp = {}

        # we don't need to build the actual string, because it won't generate duplicates
        def recursive(length):
            # if the length of the string is already greater, return 0
            if length>high:
                return 0
            # if the length is already calculated, add it
            if length in dp:
                return dp[length]

            # check the bottom boundary
            if length>=low:
                dp[length] = 1
            else:
                dp[length] = 0
            # calculate the result recursively
            dp[length] += recursive(length+zero) + recursive(length+one)

            return dp[length] % module
        
        return recursive(0)