class Solution:
    def decodeString(self, s: str) -> str:
        ans=""

        st, num=[], 0
        for x in s:
            if x.isnumeric():
                num=num*10+int(x)
            # collect the resource in the brackets []
            elif x=='[':
                st.append(ans)
                st.append(num)
                ans=""
                num=0
            # stop 
            elif x==']':
                # this will be the number before the bracket
                tmp=st.pop()
                # this will be the str before the number
                prev=st.pop()
                ans=prev+tmp*ans
            # hold the str between the brackets and the answer
            else:
                ans+=x
        return ans