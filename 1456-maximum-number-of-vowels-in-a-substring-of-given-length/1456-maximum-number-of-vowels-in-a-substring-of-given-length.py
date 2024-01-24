class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        maxV, tmp = 0, 0
        for x in range(0, k):
            if s[x] in vowels:
                maxV += 1
        tmp = maxV
        for x in range(0, len(s)-k):
            if s[x] in vowels:
                tmp -= 1
            if s[x+k] in vowels:
                tmp += 1
            maxV = max(maxV, tmp)
        return maxV