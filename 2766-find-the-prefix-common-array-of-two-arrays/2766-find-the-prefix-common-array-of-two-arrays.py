class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        freq = {}
        count = 0
        res = [0]*len(A)

        for x in range(len(A)):
            if A[x] not in freq:
                freq[A[x]] = 1
            else:
                count += 1
                freq.pop(A[x])
            
            if B[x] not in freq:
                freq[B[x]] = 1
            else:
                count += 1
                freq.pop(B[x])
            
            res[x] = count
        
        return res