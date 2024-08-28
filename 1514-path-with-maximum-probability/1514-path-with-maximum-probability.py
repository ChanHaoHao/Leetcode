class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # store all the paths in a hash map
        linked_map = {}
        for x in range(len(edges)):
            start, end, prob = edges[x][0], edges[x][1], succProb[x]
            if start not in linked_map:
                linked_map[start] = {(end, prob)}
            else:
                linked_map[start].add((end, prob))
            if end not in linked_map:
                linked_map[end] = {(start, prob)}
            else:
                linked_map[end].add((start, prob))

        # create a max-heap for the process to find the max probability
        # start from the start node
        heap = [(-1, start_node)]
        visited = set()
        while heap:
            prob, curr = heapq.heappop(heap)
            visited.add(curr)

            # if the end_node is met
            if curr==end_node:
                return prob*-1
            
            # if it reached a dead end
            if curr not in linked_map:
                break
            
            # heappush the next probability into the heap
            for node, next_prob in linked_map[curr]:
                if node not in visited:
                    heapq.heappush(heap, (prob*next_prob, node))
        
        return 0