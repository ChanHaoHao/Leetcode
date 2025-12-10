class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        history = {}
        for i, n in enumerate(nums):
            if n in history:
                if i-history[n]<=k:
                    return True
                history[n] = i
            else:
                history[n] = i
        return False