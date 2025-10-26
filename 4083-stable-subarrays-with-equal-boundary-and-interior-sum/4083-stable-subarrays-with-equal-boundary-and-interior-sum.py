class Solution:
    def countStableSubarrays(self, capacity: List[int]) -> int:
        # Find all possible subsets and iterate through, TLE
        # count = Counter(capacity)

        # cands = []
        # for i in count.keys():
        #     if count[i]>=2:
        #         cands.append(i)

        # ans = 0
        # for cand in cands:
        #     indices = [capacity.index(cand)]
        #     while True:
        #         if indices[-1]+1 < len(capacity) and cand in capacity[indices[-1]+1::]:
        #             indices.append(indices[-1]+1+capacity[indices[-1]+1::].index(cand))
        #         else:
        #             break

        #     for i in range(len(indices)-1):
        #         for j in range(len(indices)-1, i, -1):
        #             l, r = indices[i], indices[j]

        #             if r-l < 2:
        #                 break
        #             elif capacity[l]==capacity[r]==sum(capacity[l+1:r]):
        #                 ans += 1
        # return ans

        prefix = [capacity[0]]
        dp = defaultdict(set)
        dp[(capacity[0], capacity[0])].add(0)

        res = 0
        for i in range(1, len(capacity)):
            # get the sum from the first index to the current index
            pref = capacity[i] + prefix[-1]
            prefix.append(pref)
            dp[(pref, capacity[i])].add(i)
            # find all valid conditions
            prevprefix = (pref - capacity[i]*2, capacity[i])
            
            # len(dp[prevprefix]) finds the amount of valid conditions in dp
            # sum([1 for x in [i, i-1] if x in dp[prevprefix]]) check if the length is >= 3
            res += len(dp[prevprefix]) - sum([1 for x in [i, i-1] if x in dp[prevprefix]])   

        return res