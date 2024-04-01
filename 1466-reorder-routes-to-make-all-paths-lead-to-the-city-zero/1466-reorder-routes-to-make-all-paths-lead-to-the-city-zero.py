class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # store all the routes in the hashmap
        routes = {(start, end) for start, end in connections}
        # store the neighbors in the hashmap
        neighbors = {city:[] for city in range(n)}
        # record the visited cities
        visited = set()
        changes = 0

        # initialize all the neighbors, regardless the directions
        for a, b in connections:
            neighbors[a].append(b)
            neighbors[b].append(a)

        # recursively go through all the neighbors
        def dfs(city):
            nonlocal routes, neighbors, visited, changes

            for neighbor in neighbors[city]:
                if neighbor in visited:
                    continue

                # since the city starts from 0, so it will go through all the neighbors in the correct order
                if (neighbor, city) not in routes:
                    changes+=1
                visited.add(neighbor)
                dfs(neighbor)

        visited.add(0)
        dfs(0)

        return changes