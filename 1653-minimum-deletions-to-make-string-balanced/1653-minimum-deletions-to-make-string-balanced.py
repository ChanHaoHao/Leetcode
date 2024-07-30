class Solution:
    def minimumDeletions(self, s: str) -> int:
        # store the "A"s after and "B"s before the current index
        ABs = [0, 0]

        # because I start from the first char, so only count the "A"s after the current index
        for x in s:
            if x=='a':
                ABs[0] += 1
        
        ans = ABs[0]
        # start from index==0 to deal with len(s)==1
        for x in range(len(s)):
            if s[x]=='a':
                ABs[0] -= 1
            else:
                ABs[1] += 1

            if sum(ABs)<ans:
                ans = sum(ABs)
        
        return ans