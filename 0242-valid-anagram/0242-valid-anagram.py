class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count = defaultdict(int)

        if len(s)!=len(t):
            return False
        
        for i in range(len(s)):
            count[s[i]] += 1
            count[t[i]] -= 1
        
        for k in count.keys():
            if count[k]!=0:
                return False
        
        return True