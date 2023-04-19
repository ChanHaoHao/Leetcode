class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged=[]
        index1, index2=0, 0
        while len(merged)<(len(nums1)+len(nums2))/2:
            if index1==len(nums1):
                merged.append(nums2[index2])
                index2+=1
            elif index2==len(nums2):
                merged.append(nums1[index1])
                index1+=1
            else:
                if nums1[index1]>nums2[index2]:
                    merged.append(nums2[index2])
                    index2+=1
                else:
                    merged.append(nums1[index1])
                    index1+=1

        if (len(nums1)+len(nums2))%2==0:
            if index1==len(nums1):
                return (merged[-1]+nums2[index2])/2
            elif index2==len(nums2):
                return (merged[-1]+nums1[index1])/2
            else:
                return (merged[-1]+min(nums1[index1], nums2[index2]))/2
        return merged[-1]