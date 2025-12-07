class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        ans = 0

        for n in list(nums):
            if n+1 not in nums:
                count = 1
                tmp = n
                while tmp-1 in nums:
                    count += 1
                    tmp -= 1
                ans = max(ans, count)
        
        return ans