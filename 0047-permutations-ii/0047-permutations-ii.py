class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        counts={ n:0 for n in nums }
        for n in nums:
            counts[n]+=1
                
        ans=[]
        tmp=[]
        def dfs():
            if len(tmp)==len(nums):
                ans.append(tmp.copy())
                return
            
            for n in counts:
                if counts[n]>0:
                    tmp.append(n)
                    counts[n]-=1
                    
                    dfs()
                    
                    counts[n]+=1
                    tmp.pop()
                    
        dfs()
        return ans
            
        