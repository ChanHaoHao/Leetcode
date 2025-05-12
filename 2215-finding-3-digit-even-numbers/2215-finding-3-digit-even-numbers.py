class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        ans = set()
        count = Counter(digits)

        def backtrack(num, length):
            if length==3 and num%2==0:
                ans.add(num)
                return
            
            for x in range(10):
                if count[x]==0 or not count[x]:
                    continue
                
                if length==0 and x==0:
                    continue

                count[x] -= 1
                next_num = 10*num+x
                if length<=2:
                    backtrack(next_num, length+1)

                count[x] += 1
        
        backtrack(0, 0)
        return sorted(list(ans))
