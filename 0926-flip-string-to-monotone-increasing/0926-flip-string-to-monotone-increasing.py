class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        # prefix1 = [0]*(len(s)+1)
        # for i in range(len(s)):
        #     prefix1[i+1] = prefix1[i] + (1 if s[i]=="1" else 0)
        
        # res = len(s)
        # for i in range(0, len(s)+1):
        #     # prefix1[i] -> flip the 1s in left to 0 at index i
        #     # (len(s) - i - prefix1[-1]+prefix1[i]) -> flip the 0s in the right to 1 at index i
        #     res = min(res, prefix1[i] + (len(s) - i - prefix1[-1]+prefix1[i]))
        # return res

        res, one, changed = 0, 0, 0
        for c in s:
            if c=='1':
                one += 1
            # if there is a zero, we count if flipping previous 1s or 0s use less step
            else:
                res = min(one, changed+1)
                if res==changed+1:
                    changed += 1
        return res