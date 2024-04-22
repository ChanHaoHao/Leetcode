class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # initial thought, use bfs to go through each step by step
        ans = 0
        q = deque()
        visited = set(deadends)
        q.append("0000")

        if "0000" in visited:
            return -1

        visited.add("0000")
        
        while q:
            n = len(q)
            # bfs for all the possibilities on the same level
            for _ in range(n):
                current = q.popleft()

                if current==target:
                    return ans

                # go through all the possibilities in each index
                for x in range(4):
                    switch_index = current[x]
                    # special cases for "0" and "9"
                    if switch_index=="0":
                        prev_str = current[0:x]+"9"+current[x+1::]
                        if prev_str not in visited:
                            q.append(prev_str)
                            visited.add(prev_str)

                        next_str = current[0:x]+"1"+current[x+1::]
                        if next_str not in visited:
                            q.append(next_str)
                            visited.add(next_str)
                    elif switch_index=="9":
                        prev_str = current[0:x]+"8"+current[x+1::]
                        if prev_str not in visited:
                            q.append(prev_str)
                            visited.add(prev_str)

                        next_str = current[0:x]+"0"+current[x+1::]
                        if next_str not in visited:
                            q.append(next_str)
                            visited.add(next_str)
                    else:
                        prev_str = current[0:x]+str(int(switch_index)-1)+current[x+1::]
                        if prev_str not in visited:
                            q.append(prev_str)
                            visited.add(prev_str)
                        
                        next_str = current[0:x]+str(int(switch_index)+1)+current[x+1::]
                        if next_str not in visited:
                            q.append(next_str)
                            visited.add(prev_str)
            # add one for the next level
            ans += 1
        
        return -1