class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seperated=[]
        for x in strs:
            tmp=sorted(list(x))
            seperated.append(tmp)
        found=[]
        ans=[]
        for x in range(len(strs)-1):
            if x in found:
                continue
            cur=[strs[x]]
            found.append(x)
            tmp=seperated[x]
            for y in range(x+1, len(strs)):
                seperated_tmp=seperated[y]
                if seperated_tmp==tmp:
                    cur.append(strs[y])
                    found.append(y)
            ans.append(cur)

        if len(strs)-1 not in found:
            ans.append([strs[-1]])
        return ans