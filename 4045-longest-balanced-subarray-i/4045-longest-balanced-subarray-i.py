class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n=len(nums)
        m=0
        # brute force, start from each index
        for i in range(n):
            e=set()
            o=set()
            # go all the way to the end
            for j in range(i,n):
                if nums[j]%2==0:
                    e.add(nums[j])
                else:
                    o.add(nums[j])
                # if from i to n, there are any subarray is balanced update the ans
                if(len(e)==len(o)):
                    m=max(j-i+1,m)
               
        return m
                        