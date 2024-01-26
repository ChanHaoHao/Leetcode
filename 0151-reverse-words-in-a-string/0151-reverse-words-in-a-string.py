class Solution:
    def reverseWords(self, s: str) -> str:
        # split the str first, then pop the list to reverse
        split_str = s.split(" ")

        ans = ""
        while len(split_str)>0:
            tmp = split_str.pop()
            # if tmp is not None
            if tmp:
                ans+=tmp+" "
        return ans[0:-1]