class Solution:
    def minLength(self, nums: List[int], k: int) -> int:
        # ans, left, right, sub, distinct = -1, 0, 0, 0, defaultdict(int)
        # while right<len(nums):
        #     distinct[nums[right]] += 1
        #     if distinct[nums[right]]>1:
        #         right += 1
        #         continue

        #     sub += nums[right]
        #     right += 1
            
        #     while left<right and sub>=k:
                
        #         if ans==-1:
        #             ans = right-left
        #         else:
        #             ans = min(ans, right-left)

        #         distinct[nums[left]] -= 1
        #         if distinct[nums[left]] == 0:
        #             sub -= nums[left]
        #         left += 1


        # return ans

        freq = Counter()
        l = 0
        ans = inf
        for r, n in enumerate(nums):
            freq[n] += 1
            # if it is a distinct number
            if freq[n]==1:
                k -= n
            # if the current summation is greater than k
            while k <= 0:
                ans = min(ans, r-l+1)
                freq[nums[l]] -= 1
                if freq[nums[l]] == 0:
                    k += nums[l]
                l += 1
        
        if ans<inf:
            return ans
        else:
            return -1