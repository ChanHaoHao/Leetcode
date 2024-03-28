class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [1]*len(rooms)
        visited[0]=0
        keys = []
        for x in rooms[0]:
            keys.append(x)

        # while there are keys remaining
        while keys:
            key = keys.pop()

            # if the room is visited
            if visited[key]==0:
                continue
            visited[key] = 0
            # append all keys for rooms that are not visited
            for x in rooms[key]:
                if visited[x]:
                    keys.append(x)

        if sum(visited):
            return False
        return True