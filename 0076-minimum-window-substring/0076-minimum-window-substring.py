class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
            return ""

        # use count, curr as a hashmap to store elements
        count, curr ={}, {}
        for x in t:
            count[x] = 1+count.get(x, 0)
        
        # use left, right as two pointers
        # store the different elements in meet_require
        meet_require, required = 0, len(count)
        left, ans= 0, [0, float("inf")] 
        for right in range(len(s)):
            char = s[right]
            if char in count:
                curr[char] = 1+curr.get(char, 0)
                # if the require is met
                if curr[char]==count[char]:
                    meet_require += 1
                    # start moving the left pointer to make the string smaller
                    while meet_require==required:
                        if (right-left+1)<ans[1]-ans[0]+1:
                            ans = [left, right]

                        if s[left] in count:
                            curr[s[left]] -= 1
                            if curr[s[left]]<count[s[left]]:
                                meet_require -= 1
                        left += 1
        
        if ans[1]!=float("inf"):
            return s[ans[0]:ans[1]+1]
        return ""        

                
