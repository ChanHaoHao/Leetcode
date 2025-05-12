class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        # first store the answer in a set
        ans = set()
        # count the frequency of the digits
        count = Counter(digits)

        def backtrack(num, length):
            # if it is three digits and an even number
            if length==3 and num%2==0:
                ans.add(num)
                return
            
            # try every valid possibility and see we can add the number or not
            for x in range(10):
                if count[x]==0 or not count[x]:
                    continue
                
                # don't let the number to start with 0
                if length==0 and x==0:
                    continue

                count[x] -= 1
                next_num = 10*num+x
                if length<=2:
                    backtrack(next_num, length+1)

                count[x] += 1
        
        backtrack(0, 0)
        return sorted(list(ans))
