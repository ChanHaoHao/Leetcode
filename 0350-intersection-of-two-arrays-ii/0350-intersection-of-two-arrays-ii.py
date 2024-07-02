class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersect = []

        nums1.sort()
        nums2.sort()

        def find_intersect(nums1, nums2):
            index1, index2, n1, n2 = 0, 0, len(nums1), len(nums2)

            while index1<n1 and index2<n2:
                if nums1[index1]==nums2[index2]:
                    intersect.append(nums1[index1])
                    index1 += 1
                    index2 += 1
                elif nums1[index1]>nums2[index2]:
                    index2+=1
                else:
                    index1+=1

        if len(nums1)>len(nums2):
            find_intersect(nums1, nums2)
        else:
            find_intersect(nums2, nums1)

        return intersect