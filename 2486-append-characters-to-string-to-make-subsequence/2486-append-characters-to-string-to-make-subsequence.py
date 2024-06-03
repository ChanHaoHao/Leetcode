class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        s_index, t_index, n, m = 0, 0, len(s), len(t)

        # Go through s and find the first character that match t[0]
        while s_index<n:
            if s[s_index]==t[t_index]:
                # Go through both s and t
                while t_index<m and s_index<n:
                    # if s[s_index]==t[t_index] increment both variables, otherwise increment s only
                    if s[s_index]==t[t_index]:
                        t_index+=1
                        if t_index==m:
                            return 0
                    s_index+=1
            s_index+=1
        
        return m-t_index