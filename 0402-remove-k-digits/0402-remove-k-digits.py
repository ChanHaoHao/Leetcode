class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num)==k:
            return "0"

        current_index = 0
        # make num in a ascending order, and it will generate the smallest possible num
        while current_index<len(num)-1 and k>0:
            # if the next number is smaller than the current number
            # remove the current_number, and check the previous number
            if int(num[current_index])>int(num[current_index+1]):
                if current_index==0:
                    num = num[1::]
                else:
                    num = num[0:current_index]+num[current_index+1::]
                    current_index-=1
                k-=1    
            else:
                current_index+=1

        # if num is in ascending order and we did not use all k, remove the back of num
        if k>0:
            num = num[0:-k]
        # remove num starts with 0 after process str(int(num)) will cause memory error
        while len(num)>1 and num[0]=="0":
            num = num[1::]
        return num