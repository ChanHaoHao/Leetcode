class Solution:
    def lexSmallest(self, s: str) -> str:
        n = len(s)

        t = s

        for k in range(1,n+1):
            # reverse the first k characters
            new_t = s[:k][::-1] + s[k:]
            # reverse the last k characters
            new_p = s[:-k] + s[-k:][::-1]

            # get the minimum lexicographically string
            t = min(t, new_t, new_p)

        return t 