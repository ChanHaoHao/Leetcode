class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # sort strs make it in lexicon order
        strs = sorted(strs)
        ans = ""
        # grab the smaller and largest lexicon order
        first, last = strs[0], strs[-1]
        for i in range(min(len(first), len(last))):
            if first[i]==last[i]:
                ans += first[i]
            else:
                break
        return ans