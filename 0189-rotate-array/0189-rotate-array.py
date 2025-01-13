class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)

        front = nums[-k::]
        back = nums[0:-k]

        if len(back)==0:
            return

        for x in range(len(nums)):
            if x>=k:
                nums[x] = back[x-k]
            else:
                nums[x] = front[x]