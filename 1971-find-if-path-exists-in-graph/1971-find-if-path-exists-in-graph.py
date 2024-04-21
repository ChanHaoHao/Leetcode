class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source==destination:
            return True

        s = dict()

        # save all the edges into a dict
        for edge1, edge2 in edges:
            if edge1 not in s:
                s[edge1] = [edge2]
            else:
                s[edge1].append(edge2)
            if edge2 not in s:
                s[edge2] = [edge1]
            else:
                s[edge2].append(edge1)

        # go through all the possible paths, dfs
        visited = set()
        q = deque()
        for x in s[source]:
            q.append(x)
        while q:
            current = q.pop()
            # if the node is visited before, skip
            if current in visited:
                continue
            elif destination == current:
                return True
            else:
                visited.add(current)
                for x in s[current]:
                    if x not in visited:
                        q.append(x)

        return False