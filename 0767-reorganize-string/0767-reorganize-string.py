class Solution:
    def reorganizeString(self, s: str) -> str:
        count = {}
        for c in s:
            freq = count.get(c, 0)
            count[c] = freq+1
        
        max_heap = []
        for k in count.keys():
            max_heap.append((-count[k], k))
        heapq.heapify(max_heap)
        
        ans = ""
        waitlist = None
        while len(max_heap)!=0:
            (count, c) = heapq.heappop(max_heap)
            ans += c

            if waitlist:
                heapq.heappush(max_heap, waitlist)
                waitlist = None

            if count+1 < 0:
                waitlist = (count+1, c)
        
        if waitlist:
            return ""
        return ans