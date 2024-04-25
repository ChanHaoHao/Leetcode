class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        ans = 1
        # store the possibilities in a dict
        ideal = {s[0]: 1}

        for a in s[1::]:
            # count the possible length for the current char
            tmp = 1
            for char in ideal:
                if abs(ord(char)-ord(a))<=k:
                    if ideal[char]+1>tmp:
                        tmp = ideal[char]+1
            # this will change the largest if the char already exist or create a new char
            ideal[a]=tmp
            if tmp>ans:
                ans = tmp
        

        return ans