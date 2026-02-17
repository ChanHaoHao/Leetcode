class Solution:
    def calculate(self, s: str) -> int:
        # iterate through the string, and deal with * and / first
        # remove all empty space
        s = s.replace(" ", "")

        stack = deque()
        i = 0
        while i < len(s):
            if s[i] == '*' or s[i] == '/':
                l = i+1
                # get the second number
                while (l < len(s) and '0' <= s[l] <= '9'):
                    l += 1
                second = int(s[i+1: l])
                first = stack.pop()
                if s[i] == '*':
                    stack.append(first * second)
                else:
                    stack.append(first // second)
                i = l
            elif s[i] == '+' or s[i] == '-':
                stack.append(s[i])
                i += 1
            else:
                l = i+1
                # get the number
                while (l < len(s) and '0' <= s[l] <= '9'):
                    l += 1
                stack.append(int(s[i: l]))
                i = l

        while len(stack) > 2:
            first = stack.popleft()
            oper = stack.popleft()
            second = stack.popleft()

            if oper == '+':
                stack.appendleft(first + second)
            else:
                stack.appendleft(first - second)
        
        return stack[0]