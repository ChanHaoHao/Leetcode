class Solution:
    def removeStars(self, s: str) -> str:
        # while "*" in s:
        #     s = s[0:s.index("*")-1]+s[s.index("*")+1::]
        
        # return s

        # using stack to solve, pop when you see a *
        result = []
        for x in s:
            if x == "*":
                result.pop()
            else:
                result.append(x)

        ans = ""
        for x in result:
            ans+=x
        return ans