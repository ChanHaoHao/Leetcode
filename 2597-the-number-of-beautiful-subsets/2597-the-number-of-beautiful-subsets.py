class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        ans = 0
        n = len(nums)
        # use visited to store the visited numbers
        visited = defaultdict(int)

        def backtrack(index):
            nonlocal ans
            if index==n:
                ans += 1
                return

            curr = nums[index]
            # if adding the current number will not become ugly
            if visited[curr-k]==0 and visited[curr+k]==0:
                # add the current number and go through
                visited[curr]+=1
                backtrack(index+1)
                # remove the current number and go again (skip the current number)
                visited[curr]-=1
                
            # this is for the ones that make the subarray ugly and the ones that are skipped
            backtrack(index+1)

        backtrack(0)
        return ans-1