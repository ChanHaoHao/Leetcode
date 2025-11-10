class Solution:
    def reverseWords(self, s: str) -> str:
        split = s.split(" ")
        ans = ""
        for s in split[::-1]:
            if s!='':
                ans += s + " "
        return ans[0:-1]