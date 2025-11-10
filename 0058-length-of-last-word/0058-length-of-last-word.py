class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        split = s.split(" ")
        for i in range(len(split)-1, -1, -1):
            if split[i]!='':
                return len(split[i])

        return 0