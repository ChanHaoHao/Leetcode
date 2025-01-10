class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        res = []
        max_freq = {}
        for word in words2:
            temp = {}
            for char in word:
                if char not in temp:
                    temp[char] = 0
                temp[char] += 1
            for x in temp:
                if x in max_freq:
                    if temp[x]>max_freq[x]:
                        max_freq[x] = temp[x]
                else:
                    max_freq[x] = temp[x]
        
        for word in words1:
            temp = {}
            for char in word:
                if char not in temp:
                    temp[char] = 0
                temp[char] += 1

            universal = True
            for x in max_freq:
                if x not in temp or temp[x]<max_freq[x]:
                    universal = False
                    break
            
            if universal:
                res.append(word)
        
        return res