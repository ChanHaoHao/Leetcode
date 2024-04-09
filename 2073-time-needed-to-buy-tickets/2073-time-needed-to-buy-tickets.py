class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0

        # before index k, if need more ticket than tickets[k], it will only buy tickets[k]
        # after index k, if need more ticket than tickets[k]-1, it will only buy tickets[k]-1
        for x in range(len(tickets)):
            if x<=k:
                ans+=min(tickets[k], tickets[x])
            else:
                ans+=min(tickets[k]-1, tickets[x])
        
        return ans