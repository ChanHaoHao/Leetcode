class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1, s2="", ""

        for x in s:
            if x=="#":
                if len(s1)>0:
                    s1=s1[0:-1]
            else:
                s1+=x
        for x in t:
            if x=="#":
                if len(s2)>0:
                    s2=s2[0:-1]
            else:
                s2+=x
        return s1==s2