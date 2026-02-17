class Solution:
    def calculate(self, s: str) -> int:
        def update(sign, num):
            if sign == "+":
                stack.append(num)
            elif sign == "-":
                stack.append(-num)
            elif sign == "*":
                stack.append(stack.pop() * num)
            elif sign == "/":
                stack.append(int(stack.pop() / num))

        i, num, stack, sign = 0, 0, [], "+"

        while i < len(s):
            if s[i].isdigit():
                num = num*10 + int(s[i])
            elif s[i] in "+-*/":
                update(sign, num)
                num = 0
                sign = s[i]
            i += 1
            
        update(sign, num)

        return sum(stack)