class Solution:
    def compress(self, chars: List[str]) -> int:
        ans=0

        if len(chars)==1:
            return len(chars)

        count=1
        for i in range(1, len(chars)):
            if chars[i]==chars[i-1]:
                count+=1
            else:
                chars[ans]=chars[i-1]
                ans+=1
                if count>1:
                    tmp=str(count)
                    for j in tmp:
                        chars[ans]=j
                        ans+=1
                count=1

        chars[ans]=chars[-1]
        ans+=1
        if count>1:
            tmp=str(count)
            for j in tmp:
                chars[ans]=j
                ans+=1

        return ans