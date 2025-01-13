class Solution:
    def minimumLength(self, s: str) -> int:
        res = 0
        # count the number of characters in the string
        count = Counter(s)

        for x in count:
            # if the character is geq than 3
            while count[x]>=3:
                # if count[x]//3>0:
                #     # during each iter, remove 3 and add 1 for each set
                #     tmp = count[x]//3
                #     count[x] = count[x]%3
                #     count[x] += tmp
                count[x] -= (count[x]//3)*2
            res += count[x]
        
        return res