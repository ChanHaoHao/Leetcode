class Solution:
    def fractionAddition(self, expression: str) -> str:
        runResult = []
        l, r = 0, 1
        while r<len(expression):
            if expression[r]=='-' or expression[r]=='+':
                val = expression[l:r].split('/')

                if len(runResult)==0:
                    runResult.append(int(val[0]))
                    runResult.append(int(val[1]))
                else:
                    runResult[0] = int(val[0])*runResult[1]+int(val[1])*runResult[0]
                    runResult[1] *= int(val[1])
                l = r
                r += 1
            r += 1

        if len(runResult)==0:
            return expression
        val = expression[l:r].split('/')

        runResult[0] = int(val[0])*runResult[1]+int(val[1])*runResult[0]
        runResult[1] *= int(val[1])
        if runResult[0]!=0 and runResult[1]!=0:
            gcd = self.gcd(abs(runResult[0]), abs(runResult[1]))
            return str(runResult[0]//gcd)+'/'+str(runResult[1]//gcd)

        return "0/1"

        
    def gcd(self, num1, num2):
        if num1<num2:
            tmp = num1
            num1 = num2
            num2 = tmp

        res = num1%num2
        while res!=0:
            num1 = num2
            num2 = res
            res = num1%num2
        return num2
        