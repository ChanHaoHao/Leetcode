class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # go through the list, and minus 1 everytime r meets a 0
        # when there is no more 0 can be flipped, move l and add 1 back 
        # everytime l meets a 0
        l, r = 0, 0

        for r in range(len(nums)):
            if nums[r] == 0:
                k -= 1
            if k<0:
                if nums[l] == 0:
                    k += 1
                l += 1
        return r-l+1