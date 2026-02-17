class Solution:
    def isValid(self, s: str) -> bool:
        close = {'}': '{', ']': '[', ')': '('}
        stack = []

        for c in s:
            if c not in close.keys():
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                elif stack[-1] == close[c]:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0