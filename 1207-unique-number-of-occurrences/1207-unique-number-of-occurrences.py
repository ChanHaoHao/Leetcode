class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # use dict to store the times that a number have occured
        count = dict()
        for x in arr:
            if x in count:
                count[x]+=1
            else:
                count[x]=1

        # check if there are repeated occurences
        tmp=[]
        for x in count:
            if count[x] in tmp:
                return False
            else:
                tmp.append(count[x])

        return True