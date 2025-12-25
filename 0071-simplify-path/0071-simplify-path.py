class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = []
        i, n, dots = 0, len(path), 0

        sub_path = ""
        while i<n:
            if path[i]=='/':
                if dots==2:
                    if len(sub_path)>dots:
                        paths.append(sub_path)
                    elif len(paths)>0:
                        paths.pop()
                elif not (dots==1 and len(sub_path)==1) and len(sub_path)>0:
                    paths.append(sub_path)
                sub_path = ""
                dots = 0
            else:
                if path[i]==".":
                    dots += 1
                sub_path += path[i]
            i += 1
        
        if dots==2:
            if len(sub_path)>dots:
                paths.append(sub_path)
            elif len(paths)>0:
                paths.pop()
        elif not (dots==1 and len(sub_path)==1) and len(sub_path)>0:
            paths.append(sub_path)
        
        ans = "/"
        for path in paths:
            ans += path + "/"
        if len(ans)>1:
            return ans[:-1]
        return ans
