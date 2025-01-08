class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ans = 0
        for x in range(len(words)):
            for y in range(x+1, len(words)):
                w1, w2 = words[x], words[y]
                l1 = len(words[x])
                if w2[:l1]==w1 and w2[-l1:]==w1:
                    ans += 1
        
        return ans