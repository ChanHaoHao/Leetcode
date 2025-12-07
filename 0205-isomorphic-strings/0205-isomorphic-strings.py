class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        hash_map = {}
        mapped = set()
        n = len(s)

        for i in range(n):
            if s[i] not in hash_map:
                if t[i] not in mapped:
                    hash_map[s[i]] = t[i]
                    mapped.add(t[i])
                else:
                    return False
            elif s[i] in hash_map:
                if hash_map[s[i]] != t[i]:
                    return False
            else:
                return False
        
        return True