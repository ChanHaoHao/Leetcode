class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        len1, len2 = len(nums1), len(nums2)

        ans = 0
        if len1%2:
            for x in nums2:
                ans ^= x
        if len2%2:
            for x in nums1:
                ans ^= x
        
        return ans