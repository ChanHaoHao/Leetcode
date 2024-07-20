class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        # such a poor description
        # consider the cost of workers into two arrays counting from the front and from the back, then choose between them
        head_workers = costs[0:candidates]
        # to prevent candidates is greater than k/2
        tail_workers = costs[max(candidates, len(costs)-candidates)::]
        # pointers to tell where the next candidate is
        next_head = candidates
        next_tail = len(costs)-candidates-1

        heapq.heapify(head_workers)
        heapq.heapify(tail_workers)

        ans = 0
        for _ in range(k):
            # if len(tail_workers)==0 and min(head_workers)<=min(tail_workers)
            if not tail_workers or head_workers and head_workers[0]<=tail_workers[0]:
                ans += heapq.heappop(head_workers)

                if next_head<=next_tail:
                    heapq.heappush(head_workers, costs[next_head])
                    next_head += 1
            else:
                ans += heapq.heappop(tail_workers)

                if next_head<=next_tail:
                    heapq.heappush(tail_workers, costs[next_tail])
                    next_tail -= 1
        
        return ans