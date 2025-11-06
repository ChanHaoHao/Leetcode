class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        queue = [(0, nums[0])]
        n = len(nums)

        while queue:
            index, steps = queue.pop()
            
            for i in range(1, steps+1):
                if index+i>=n-1:
                    return True
                elif nums[index+i]!=0:
                    queue.append((index+i, nums[index+i]))

        return False