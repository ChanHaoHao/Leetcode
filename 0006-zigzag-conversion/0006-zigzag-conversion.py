class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s)<=numRows or numRows==1:
            return s
        ans=""
        container=[[''] for i in range(numRows)]
        for i in range(len(s)):
            tmp=i%(numRows*2-2)
            if tmp>numRows-1:
                container[numRows*2-tmp-2].append(s[i])
            else:
                container[tmp].append(s[i])

        for i in container:
            for j in i[1::]:
                ans+=j
        return ans