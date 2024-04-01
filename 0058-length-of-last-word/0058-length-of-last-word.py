class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split(" ")

        for x in range(len(words)-1, -1, -1):
            if words[x]!="":
                return len(words[x])

        return 0