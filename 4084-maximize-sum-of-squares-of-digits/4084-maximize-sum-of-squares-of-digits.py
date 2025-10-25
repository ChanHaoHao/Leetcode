class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        # no integer will have sum of each index greater than length*9
        if sum>num*9:
            return ""

        ans = ""
        # If sum is greater than 9, put 9 in
        while sum>=9:
            ans += "9"
            sum -= 9
        # If there are remaining num, put it in
        if sum!=0:
            ans += str(sum)

        # Fill the rest with 0
        for _ in range(num-len(ans)):
            ans += "0"
        return ans