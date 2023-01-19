class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max=0
        container=[]
        for x in s:
            while x in container:
                container.pop(0)
            container.append(x)
            if len(container)>max:
                max = len(container)
        return max