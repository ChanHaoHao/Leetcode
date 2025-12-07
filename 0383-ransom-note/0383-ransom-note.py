class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        letters = [0] * 26

        for r in ransomNote:
            letters[ord(r)-ord('a')] += 1
        for m in magazine:
            letters[ord(m)-ord('a')] -= 1
        
        for i in range(26):
            if letters[i]>0:
                return False
        return True