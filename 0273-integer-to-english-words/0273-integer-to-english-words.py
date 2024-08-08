class Solution:
    def numberToWords(self, num: int) -> str:
        if num==0:
            return "Zero"

        # hash map for all distinct numbers
        distinct = {1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five",
                    6:"Six", 7:"Seven", 8:"Eight", 9:"Nine", 10:"Ten", 11:"Eleven", 
                    12:"Twelve", 13:"Thirteen", 14:"Fourteen", 15:"Fifteen", 
                    16:"Sixteen", 17:"Seventeen", 18:"Eighteen", 19:"Nineteen"}
        distinct20 = {2:"Twenty", 3:"Thirty", 4:"Forty", 5:"Fifty", 6:"Sixty", 
                        7:"Seventy", 8:"Eighty", 9:"Ninety"}

        def gen_str(n):
            res = []
            # get the number of the hundreds
            hundreds = n//100
            if hundreds:
                res.append(distinct[hundreds]+" Hundred")
            n = n%100

            # get the number of the tens
            tens = n//10
            if tens==1:
                res.append(distinct[n])
                # to stop counting the singles
                n=0
            elif tens:
                res.append(distinct20[tens])
            n = n%10

            if n:
                res.append(distinct[n])

            return " ".join(res)

        post_digit = ["", " Thousand", " Million", " Billion"]
        i = 0
        ans = []
        while num:
            digits = num%1000
            
            s = gen_str(digits)
            if s:
                # because we start from the last, so add to the front each time
                ans = [s+post_digit[i]]+ans
            num = num//1000
            i += 1

        return " ".join(ans)