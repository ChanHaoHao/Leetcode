class Solution:
    def reverseParentheses(self, s: str) -> str:
        pos = deque()
        ans = ""

        for x in s:
            if x == "(":
                pos.append(len(ans))
            # when brackets are closed, reverse the string between the brackets
            elif x == ")":
                index = pos.pop()
                tmp = ans[index::]
                ans = ans[0:index] + tmp[::-1]
            else:
                ans += x

        return ans
        