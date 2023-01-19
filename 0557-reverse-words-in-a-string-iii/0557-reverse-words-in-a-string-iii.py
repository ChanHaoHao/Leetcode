class Solution:
    def reverseWords(self, s: str) -> str:
        sol=""
        temp = s.split()
        indi=0
        for x in temp:
            for y in range(len(x)-1,-1,-1):
                sol += x[y]
            if indi == len(temp)-1:
                return sol
            indi += 1
            sol += " "
        return sol