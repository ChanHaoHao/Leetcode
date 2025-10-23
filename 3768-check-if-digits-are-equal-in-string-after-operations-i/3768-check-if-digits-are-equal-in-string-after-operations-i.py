class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s)>2:
            tmp = ""
            for x in range(len(s)-1):
                tmp += str((int(s[x]) + int(s[x+1])) % 10)                
            s = tmp

        if s[0]==s[1]:
            return True
        return False