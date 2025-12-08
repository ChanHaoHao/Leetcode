class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        t_count = defaultdict(int)
        for sub in t:
            t_count[sub] += 1

        count = len(t_count)
        n = len(s)
        l, r = 0, 0
        ans = ""
        
        while r<n:
            t_count[s[r]] -= 1
            if t_count[s[r]] == 0:
                count -= 1
            
            if count==0:
                while count==0:
                    if len(ans)==0 or len(ans)>r-l+1:
                        ans = s[l:r+1]
                    t_count[s[l]] += 1
                    if t_count[s[l]] > 0:
                        count += 1
                    
                    l += 1
            r += 1
        
        return ans