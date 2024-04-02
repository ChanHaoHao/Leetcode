class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        pairs = collections.defaultdict(list)

        # first we store all the possible equations, just like processing the neighbors in 1466
        for i, eq in enumerate(equations):
            a, b = eq
            pairs[a].append([b, values[i]])
            pairs[b].append([a, 1/values[i]])

        # using bfs to check for possible paths
        def bfs(nominator, denominator):
            if nominator not in pairs or denominator not in pairs:
                return -1

            queue, visited = deque(), set()
            # initialize the queue with the nominator and weight=1
            queue.append([nominator, 1])
            visited.add(nominator)
            while queue:
                n, w = queue.popleft()
                if n==denominator:
                    return w
                for neighbor, weight in pairs[n]:
                    # don't go to visited neighbors, since it will become loops
                    if neighbor not in visited:
                        queue.append([neighbor, w*weight])
                        visited.add(neighbor)
            # if there is no way to reach the nominator after bfs
            return -1

        ans = []
        for nominator, denominator in queries:
            ans.append(bfs(nominator, denominator))

        return ans