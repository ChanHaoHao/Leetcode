class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # changes = []
        # for i in range(len(s)-1):
        #     if s[i]!=s[i+1]:
        #         changes.append(i)
        
        # ans = 0
        # for change in changes:
        #     l, r = change, change+1
        #     ans += 1
        #     while l>0 and r<len(s)-1 and s[l-1]==s[change] and s[r+1]==s[change+1]:
        #         l -= 1
        #         r += 1
        #         ans += 1
        
        # return ans

        # count how many times 0, 1 have occured before it switched
        prev, curr = 0, 1
        ans = 0

        for i in range(1, len(s)):
            # if it hasn't switched yet
            if s[i]==s[i-1]:
                curr += 1
            else:
                ans += min(prev, curr)
                prev = curr
                curr = 1
        
        ans += min(prev, curr)
        return ans