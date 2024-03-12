# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # turn the listnodes into an array
        tmp = head
        num_list = [tmp.val]
        while tmp.next!=None:
            num_list.append(tmp.next.val)
            tmp = tmp.next

        # find out all the subarray that sums up to 0
        x=0
        while x<len(num_list):
            # check if the current num is 0
            if num_list[x]==0:
                num_list.pop(x)
                continue

            # check all the previous subarrays
            for y in range(x):
                if sum(num_list[y:x+1])==0:
                    num_list = num_list[0:y]+num_list[x+1::]
                    x = y-1
                    break
            x+=1

        # change the array back into listnode
        ans = ListNode()
        tmp = ans
        if len(num_list)>0:
            for x in num_list:
                tmp.next = ListNode(x, None)
                tmp = tmp.next

        return ans.next