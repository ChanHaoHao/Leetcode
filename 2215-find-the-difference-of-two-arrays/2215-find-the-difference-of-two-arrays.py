class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # ans = [[], []]
        # common = []

        # for x in nums1:
        #     if x not in nums2 and x not in ans[0]:
        #         ans[0].append(x)
        #     elif x not in common:
        #         common.append(x)
        # for x in nums2:
        #     if x not in common and x not in ans[1]:
        #         ans[1].append(x)

        # return ans

        # use set() to delete duplicate elements
        nums1, nums2 = set(nums1), set(nums2)
        
        return [nums1-nums2, nums2-nums1]