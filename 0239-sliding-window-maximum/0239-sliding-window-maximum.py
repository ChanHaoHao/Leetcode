class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # ans = [max(nums[0:k])]

        # for x in range(1, len(nums)-k+1):
        #     if nums[x+k-1]>ans[x-1]:
        #         ans.append(nums[x+k-1])
        #     elif nums[x-1]==ans[x-1]:
        #         ans.append(max(nums[x:x+k]))
        #     else:
        #         ans.append(ans[x-1])
        
        # return ans
        ans = []
        # store index in the window
        window = deque()
        # use two pointers to keep track
        l = 0
        for r in range(len(nums)):
            # this makes the max value index store at the front of the deque
            # and guarentees the value of the deque is in descending order
            while window and nums[window[-1]]<nums[r]:
                window.pop()
            window.append(r)

            # if the window have passed
            if l>window[0]:
                window.popleft()
            if r+1>=k:
                ans.append(nums[window[0]])
                l+=1
            
        return ans