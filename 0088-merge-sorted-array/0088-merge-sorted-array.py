class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # start from m+n-1 and put the largest value of num1 and num2 to the end of num1
        # if nums1 has used all its numbers, put nums2 in it
        # if nums2 has used all its numbers, no further action needed
        m -= 1
        n -= 1

        for x in range(len(nums1)-1, -1, -1):
            if m>=0 and n>=0:
                if nums1[m]>nums2[n]:
                    nums1[x] = nums1[m]
                    m -= 1
                else:
                    nums1[x] = nums2[n]
                    n -= 1
            else:
                if m<0:
                    nums1[x] = nums2[n]
                    n -= 1