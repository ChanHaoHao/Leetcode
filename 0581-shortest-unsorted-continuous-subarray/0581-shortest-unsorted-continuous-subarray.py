class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        check_front, check_back = True, True
        while (check_front or check_back) and len(nums)>0:
            if check_front and len(nums):
                if nums.index(min(nums))==0:
                    nums.pop(nums.index(min(nums)))
                else:
                    check_front=False
                    if check_back==False:
                        return len(nums)
                
            if check_back and len(nums):
                tmp=nums[::-1]
                if tmp.index(max(nums))==0:
                    tmp.pop(tmp.index(max(tmp)))
                    nums=tmp[::-1]
                else:
                    check_back=False
                    if check_front==False:
                        return len(nums)
        return 0