class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ans = 0
        for x in range(len(words)-1):
            for y in range(x+1, len(words)):
                if len(words[x])<=len(words[y]):
                    if words[y][0:len(words[x])]==words[x] and words[y][-len(words[x])::]==words[x]:
                        ans += 1
        
        return ans