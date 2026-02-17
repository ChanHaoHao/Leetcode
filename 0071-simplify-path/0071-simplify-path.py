class Solution:
    def simplifyPath(self, path: str) -> str:
        sub_paths = []
        split_paths = path.split('/')

        for split_p in split_paths:
            if len(split_p) == 0 or split_p == ".":
                continue
            elif split_p == "..":
                if len(sub_paths) > 0:
                    sub_paths.pop()
            else:
                sub_paths.append(split_p)
        
        ans = ""
        for sub_path in sub_paths:
            ans += "/" + sub_path
        if len(ans) == 0:
            return "/"
        return ans