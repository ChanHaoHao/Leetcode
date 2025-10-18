class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        # this guarantees that the lb will start from the first nums lb
        last_pick = nums[0] - k - 1
        ans = 0

        for num in nums:
            lb = num - k
            ub = num + k
            if last_pick < lb:
                last_pick = lb
            else:
                last_pick += 1
            
            if last_pick <= ub:
                ans += 1
            else:
                last_pick -= 1
        
        return ans