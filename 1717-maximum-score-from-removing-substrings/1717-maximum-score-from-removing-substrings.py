class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        ans = 0
        stack = deque()

        if x>y:
            high_prior = "ab"
            low_prior = "ba"
            score = [x, y]
        else:
            high_prior = "ba"
            low_prior = "ab"
            score = [y, x]

        for x in s:
            if len(stack)==0:
                stack.append(x)
            else:
                if stack[-1]+x==high_prior:
                    stack.pop()
                else:
                    stack.append(x)
        ans = ((len(s)-len(stack))//2)*score[0]

        stack2 = deque()
        for x in stack:
            if len(stack2)==0:
                stack2.append(x)
            else:
                if stack2[-1]+x==low_prior:
                    stack2.pop()
                else:
                    stack2.append(x)
        ans += ((len(stack)-len(stack2))//2)*score[1]

        return ans