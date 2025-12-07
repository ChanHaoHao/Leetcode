class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        
        split = s.split(' ')
        map1 = []
        map2 = []

        for p in pattern:
            map1.append(pattern.index(p))
        for sub in split:
            map2.append(split.index(sub))

        if map1==map2:
            return True
        return False