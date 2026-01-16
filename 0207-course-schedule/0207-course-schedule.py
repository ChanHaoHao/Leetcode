class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # pres = [[] for _ in range(numCourses)]
        # # if the degree of a course is 0, means it is not dependent
        # degree = [0]*numCourses

        # for pre in prerequisites:
        #     pres[pre[1]].append(pre[0])
        #     degree[pre[0]] += 1
        
        # # get all the course that does not require prerequisite, bfs
        # queue = deque()
        # for i in range(numCourses):
        #     if degree[i]==0:
        #         queue.append(i)
        
        # taken = []
        # while queue:
        #     curr = queue.popleft()
        #     taken.append(curr)

        #     # remove the taken prerequisite course
        #     for nxt in pres[curr]:
        #         degree[nxt] -= 1
        #         if degree[nxt]==0:
        #             queue.append(nxt)
        
        # return len(taken)==numCourses

        pres = [[] for _ in range(numCourses)]
        for pre in prerequisites:
            pres[pre[1]].append(pre[0])
        # 0: unvisited, 1: visiting, 2: processed
        visited = [0] * numCourses 

        def dfs(course):
            # cycle detected
            if visited[course] == 1:
                return False
            # already checked
            if visited[course] == 2:
                return True
            
            # currently checking
            visited[course] = 1
            for pre in pres[course]:
                if not dfs(pre):
                    return False
            
            # finished checking
            visited[course] = 2
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True
