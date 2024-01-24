# this method goes through all the possible combinations
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        result = [0]
        self.dfs(arr, "", 0, result)
        return result[0]

    def dfs(self, arr, path, idx, result):
        # try if the path is unique
        unique = True
        for x in range(len(path)-1, 0, -1):
            if path[x] in path[0:x]:
                unique = False
                break
        if unique:
            result[0] = max(result[0], len(path))

        if idx == len(arr) or not unique:
            return

        # using this for loop as the method to check each possible combination
        # keep starting a for loop after the current subarray
        for i in range(idx, len(arr)):
            self.dfs(arr, path + arr[i], i + 1, result)