class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        ans = {}
        for s in strs:
            sorted_s = sorted(s)
            sorted_s = ''.join(sorted_s)
            if sorted_s in ans:
                ans[sorted_s].append(s)
            else:
                ans[sorted_s] = [s]
        
        res = []
        for key in ans.keys():
            res.append(ans[key])
        return res
        