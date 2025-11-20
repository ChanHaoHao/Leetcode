class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        subarray = []
        count = 0
        for word in words:
            # store the word in a subarray, if it follows the rules
            if count+len(word)+len(subarray)<=maxWidth:
                subarray.append(word)
                count += len(word)
            else:
                tmp = ""
                # if there is more than one word in the subarray
                if len(subarray)>1:
                    # how many space should be between each word
                    space = (maxWidth - count) // (len(subarray)-1)
                    # how many space+1 should have
                    large_space = (maxWidth - space*(len(subarray)-1) - count)
                    for i, sub in enumerate(subarray):
                        tmp += sub
                        if i==len(subarray)-1:
                            continue
                        elif i<large_space:
                            tmp += " "*(space+1)
                        else:
                            tmp += " "*space
                else:
                    tmp = subarray[0] + " "*(maxWidth-count)
                subarray = [word]
                count = len(word)
                ans.append(tmp)

        tmp = ""
        for sub in subarray:
            tmp += sub + " "
        tmp = tmp[0:-1]
        if len(tmp)<maxWidth:
            tmp += " "*(maxWidth-len(tmp))
        ans.append(tmp)
        
        return ans