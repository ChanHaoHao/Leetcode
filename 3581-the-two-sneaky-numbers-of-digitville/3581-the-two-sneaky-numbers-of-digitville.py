class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        count = set()

        for num in nums:
            if num in count:
                ans.append(num)
                if len(ans)==2:
                    return ans
            count.add(num)