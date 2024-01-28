class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ans = 0

        # while len(nums)>=2:
            # tmp = nums.pop()
            # if k-tmp in nums:
                # ans += 1
                # nums.pop(nums.index(k-tmp))

        nums = sorted(nums)
        l, r = 0, len(nums)-1

        while l<r:
            if nums[l]+nums[r]==k:
                ans += 1
                l += 1
                r -= 1
            else:
                if nums[l]+nums[r]>k:
                    r -= 1
                else:
                    l += 1

        return ans