class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # turn the numbers into a set
        count = set(nums)
        ans = 0
        # iterate through all the numbers in nums
        for num in list(count):
            # if num-1 DNE in the set, means that num can be a head
            if num-1 not in count:
                tmp = 1
                # find the end of the sequence
                while num+1 in count:
                    num += 1
                    tmp += 1
                ans = max(ans, tmp)
        
        return ans